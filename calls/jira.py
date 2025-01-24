import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class Jira:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

    def get_custom_field_context(self, fieldId, contextId):
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
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

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
            auth=self.token
        )

        return response

    def add_issue_link(self, inward_issue_key, outward_issue_key, link_type):
        url = self.jira + 'issueLink'
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "type": {
                "name": link_type
            },
            "inwardIssue": {
                "key": inward_issue_key
            },
            "outwardIssue": {
                "key": outward_issue_key
            }
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            json=payload,
            auth=self.token
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
            auth=self.token
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
            auth=self.token
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
            auth=self.token
        ).text)

        return response

    def all_fields(self):
        url = self.jira + "customFields?maxResults=2200"

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

    def set_project_workflow_scheme(self, key):
        url = self.jira + 'project/' + key + '/workflowscheme'

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

    def post_issue_type_scheme(self, scheme, keys):
        url = self.jira + 'issuetypescheme/' + scheme + '/associations'

        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            'idsOrKeys': keys
        }

        response = json.loads(requests.request(
            "POST",
            url,
            headers=headers,
            json=payload,
            auth=self.token
        ).text)

        return response

    def unarchive_project(self, key):
        url = self.jira + 'project/' + key + '/restore'

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        )

        if response.status_code == 200:
            return response.json()  # Use response.json() for automatic parsing
        elif response.status_code == 202:
            return {"message": "Request accepted and processed successfully, but no immediate response."}
        else:
            return {"error": f"Request failed with status code: {response.status_code}", "content": response.text}

    def archive_project(self, key):
        url = self.jira + 'project/' + key + '/archive'

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            return {"message": "Request accepted and processed successfully, but no immediate response."}
        else:
            return {"error": f"Request failed with status code: {response.status_code}", "content": response.text}

    def assign_ticket(self, key, username):
        url = self.jira + f'issue/{key}/assignee'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "name": username
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response

    def find_users_by_string(self, string, max_result, start_at):
        url = self.jira + 'user/search'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        query = {
            'username': string,
            "startAt": start_at,
            'maxResults': max_result
        }

        users = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return users

    def update_ticket(self, key, payload):
        url = self.jira + 'issue/' + key
