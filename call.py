import requests
from auth import auth, staging_auth, okta_token, conf_token, staging_conf_token
import json
from config import confluence, jira, jira_staging, confluence_staging
import urllib.parse
from datetime import datetime


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence

    def conf_call(self, pref):
        url = self.conf_url + pref

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    @classmethod
    def get_child_pages_recursive(cls, pref):
        url = f'content/{pref}/child/page?limit=500&expand=version'
        response = Confluence.conf_call(url)

        pages = response["results"]
        page_dicts = []

        for page in pages:
            page_dict = {
                "id": page["id"],
                "title": page["title"],
                "children": cls.get_child_pages_recursive(page["id"])
            }
            print(page['id'])
            page_dicts.append(page_dict)

        return page_dicts

    def move_page(self, pref, version, ancestors):
        url = self.conf_url + f'content/{pref}'

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        payload = json.dumps({
            "version": {
                "number": version,
            },
            "title": "testing more page",
            "type": "page",
            "ancestors": [
                {
                    "id": ancestors
                }
            ]})

        response = json.loads(requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers
        ).text)

        return response


def call(pref, apiAction, payload=''):
    url = jira + pref

    if apiAction == 'get':
        headers = {"Accept": "application/json"}
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text)

    elif apiAction == 'search':
        url = f'https://jira.robot.car/rest/api/2/search?jql={pref}'
        headers = {
            "Accept": "application/json"
        }
        query = {
            'jql': pref,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text)

    elif apiAction == 'put':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = json.loads(requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=auth
        ).text)

    elif apiAction == 'post':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        ).text)

    elif apiAction == 'groups':
        url = f'https://jira.robot.car/rest/api/2/{pref}'
        headers = {
            "Accept": "application/json"
        }
        query = {
            'username': payload,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            params=query,
            headers=headers,
            auth=auth
        ).text)

    return response


def field_metrics():
    url = "https://jira.robot.car/rest/api/2/customFields?maxResults=2200"

    headers = {
        "Accept": "application/json"
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    return response


def status_metrics():
    url = "https://jira.robot.car/rest/api/2/status"

    headers = {
        "Accept": "application/json"
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    return response


def project_metric(key):
    url = f"https://jira.robot.car/rest/api/2/search?maxResults=1"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'jql': f'project = {key} ORDER BY created DESC'
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

    try:
        total = response['total']
    except KeyError:
        return 0, "Project not used"
    if total == 0:
        return 0, "Project not used"
    date = datetime.strptime(response['issues'][0]['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
    lastTicketDate = date.strftime('%B %Y')
    lastTicket = response['issues'][0]['key']

    query = {
        'jql': f'project = {key} ORDER BY created ASC'
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

    date = datetime.strptime(response['issues'][0]['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
    firstTicketDate = date.strftime('%B %Y')
    firstTicket = response['issues'][0]['key']

    return total, lastTicket, lastTicketDate, firstTicket, firstTicketDate


def staging_call(pref, apiAction, payload=''):
    url = "https://jira.stage.robot.car/rest/api/2/" + pref

    if apiAction == 'get':
        headers = {"Accept": "application/json"}
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=staging_auth
        ).text)

    elif apiAction == 'put':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = json.loads(requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=staging_auth
        ).text)

    elif apiAction == 'post':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=staging_auth
        ).text)

    return response


class Okta:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def okta_call(cls, email):
        url = 'https://cruise.okta.com/api/v1/users'
        email = email
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            manager = json.loads(response.text)[0]['profile']['manager']
            if not manager:
                return 'empty'
            else:
                return manager
        except KeyError:
            return 'No Manager'
        except IndexError:
            return 'Nothing for this one'

    @classmethod
    def okta_groups(cls, name):
        url = f'https://cruise.okta.com/api/v1/groups?q={name}'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)

        id = json.loads(response.text)[0]['id']

        url = f'https://cruise.okta.com/api/v1/groups/{id}/users'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)

        return json.loads(response.text)
        # example
        # for j in admins:
        #     try:
        #         response = Okta.okta_groups(j)
        #         for name in response:
        #             manager = Okta.okta_call(name['profile']['email'])
        #             if manager != 'No Manager' and manager != 'Nothing for this one':
        #                 writer.writerow([name['profile']['email'], j, 'System Administrator', manager])
        #             print(name['profile']['email'], j, 'System admin', manager)
        #     except IndexError:
        #         response = call(f'group/member?groupname={j}', 'get')
        #         try:
        #             for i in response['values']:
        #                 manager = Okta.okta_call(i['emailAddress'])
        #                 if manager != 'No Manager' and manager != 'Nothing for this one':
        #                     writer.writerow([i['emailAddress'], j, 'Jira Administrator', manager])
        #                 print(i['displayName'], i['emailAddress'], j, 'System Administrator', manager)
        #         except KeyError:
        #             print(j)
