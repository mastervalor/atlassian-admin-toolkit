import requests
from auth import auth, staging_auth, okta_token, conf_token, staging_conf_token
import json
from config import confluence, jira, jira_staging, confluence_staging, conf_base
import urllib.parse
from datetime import datetime


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence
        self.conf_base = conf_base


    def get_user(self, username):
        url = self.conf_url + f'user?username={username}'
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}
        print(url)
        print(headers)
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response


    @classmethod
    def user_groups(cls, pref):
        url = confluence + f"user/memberof?username={pref}"

        headers = {
            "Authorization": conf_token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    def group_members(self, pref):
        url = self.conf_base + pref
        print(url)
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

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
        print(response)
        return response

    def get_child_pages_recursive(self, pref):
        url = f'content/{pref}/child/page?limit=500&expand=version'
        response = self.conf_call(url)

        pages = response["results"]
        page_dicts = []

        for page in pages:
            page_dict = {
                "id": page["id"],
                "title": page["title"],
                "children": self.get_child_pages_recursive(page["id"])
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
            "space": {
                "key": "T2"
            },
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


class Jira:
    def __init__(self, is_staging=False):
        self.token = auth
        self.jira = jira_staging if is_staging else jira

    def get_customField_context(self, fieldId, contextId):
        url = self.jira + f'customFields/{fieldId}/context/{contextId}'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_user(self, payload, pref=''):
        url = self.jira + 'user' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'username': payload,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def get_project(self, key):
        url = self.jira + 'project/' + key

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_project_groups(self, key, role_id):
        url = self.jira + 'project/' + key + '/role/' + role_id

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_projects(self):
        url = self.jira + 'project'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_project_permissionscheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme?expand=permissions'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def assign_permission_scheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def restore_project(self, key):
        url = self.jira + 'project/' + key + '/restore'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def user_groups(self, user):
        groups = self.get_user(user, '?expand=groups')
        user_groups = []

        for group in groups['groups']['items']:
            user_groups.append(group['name'])

        return user_groups

    def create_ticket(self, ticket):
        url = self.jira + 'issue'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(ticket)

        response = json.loads(requests.request(
            "POST",
            url,
            headers=headers,
            data=payload,
            auth=self.token
        ).text)

        return response

    def jql(self, pref, payload):
        url = self.jira + 'search' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'jql': payload,
        }
        print(url)
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def tickets(self, query):
        startAt = 0
        maxResults = 1000
        total = 1001
        ticket_list = []

        while total >= maxResults:
            tickets = self.jql(f'?startAt={startAt}&maxResults={maxResults}', query)

            for ticket in tickets['issues']:
                key = ticket['key'].split("-")[0]
                if key not in ticket_list:
                    ticket_list.append(key)

            print(ticket_list)
            total = tickets['total']
            startAt += 1000
            maxResults += 1000

        return ticket_list

    def get_group(self, pref, group):
        url = self.jira + 'group/member' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'groupname': group
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def group_members(self, group):
        startAt = 0
        maxResults = 50
        total = 51
        members_list = []

        while total >= maxResults:
            members = self.get_group(f'?includeInactiveUsers=false&startAt={startAt}&maxResults={maxResults}', group)

            for member in members['values']:
                members_list.append(member['name'])

            total = members['total']
            startAt += 50
            maxResults += 50
            # print(startAt, maxResults)
        return members_list

    def project_owners(self, keys):
        project_owners = []

        for key in keys:
            url = self.jira + 'project/' + key
            headers = {"Accept": "application/json"}
            response = json.loads(requests.request(
                "GET",
                url,
                headers=headers,
                auth=self.token
            ).text)
            project_owners.append([key, response['lead']['name']])

        return project_owners

    def project_owner(self, key):

        url = self.jira + 'project/' + key
        headers = {"Accept": "application/json"}
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)
        try:
            owner = response['lead']['name']
            status = response['lead']['active']
        except KeyError:
            owner = None
            status = None

        return owner, status

    def edit_ticket(self, key, payload):
        url = self.jira + 'issue/' + key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload,
            auth=auth
        )

        return response

    def get_my_permissions(self):
        url = self.jira + 'mypermissions'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text)

        return response

    def get_ticket(self, key):
        url = self.jira + 'issue/' + key + '?notifyUsers=false'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text)

        return response

    def plugins(self):
        url = self.jira + 'plugins/'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text)

        return response

    def get_projects_with_owners(self):
        url = self.jira + 'project?expand=lead'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
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
        url = f'https://jira.robot.car/rest/api/2/search?maxResults=20000'
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
            params=query,
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
            auth=staging_auth
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

    elif apiAction == 'members':
        url = jira + pref
        headers = {
            "Accept": "application/json"
        }
        query = {
            'groupname': payload,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
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
    def __init__(self, name, email, id, user_id, group_id):
        self.name = name
        self.email = email
        self.id = id
        self.users_id = user_id
        self.group_id = group_id

    @classmethod
    def users_id(cls, email):
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
            return json.loads(response.text)[0]
        except IndexError:
            return False

    # @classmethod
    # def users_manager(cls, email):
    @classmethod
    def get_user_groups(cls, id):
        groups_url = f'https://cruise.okta.com/api/v1/users/{id}/groups'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }
        response = requests.get(groups_url, headers=headers, timeout=9000)
        groups_json = response.json()
        groups = [group['profile']['name'] for group in groups_json]
        return groups

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

    @classmethod
    def get_group_id(cls, name):
        url = 'https://cruise.okta.com/api/v1/groups'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response = json.loads(response.text)
        for i in response:
            if i['profile']['name'] == name:
                return i['id']
        else:
            return f"Failed to retrieve group ID. Status code: {response.status_code}"

        return None

    @classmethod
    def add_user_to_group(cls, user_id, group_id):
        url = f"https://cruise.okta.com/api/v1/groups/{group_id}/users/{user_id}"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }
        response = requests.put(url, headers=headers)
        return response.status_code

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
