import requests
from requests.auth import HTTPBasicAuth
from auth import auth, staging_auth, email
import json
from config import jira, jira_staging


class ProjectJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira
        self.auth = HTTPBasicAuth(email, self.token)

    def get_project(self, key):
        url = self.jira + 'project/' + key

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
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
            auth=self.auth
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
            auth=self.auth
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
            auth=self.auth
        ).text)

        return response

    def get_projects_with_archived(self):
        url = self.jira + 'project'

        headers = {
            "Accept": "application/json"
        }

        query = {
            'includeArchived': True,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.auth
        ).text)

        return response

    def get_project_permission_scheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme?expand=permissions'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def assign_project_permission_scheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.auth
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
            auth=self.auth
        ).text)

        return response

    def project_owner(self, key):
        url = self.jira + 'project/' + key

        headers = {"Accept": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        try:
            owner = response['lead']['name']
            status = response['lead']['active']
        except KeyError:
            owner = None
            status = None

        return owner, status

    def set_project_workflow_scheme(self, key):
        url = self.jira + 'project/' + key + '/workflowscheme'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.auth
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
            auth=self.auth
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
            auth=self.auth
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            return {"message": "Request accepted and processed successfully, but no immediate response."}
        else:
            return {"error": f"Request failed with status code: {response.status_code}", "content": response.text}

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
            auth=self.auth
        ).text)

        return response

    def add_group_by_role(self, group, role, project_key):
        url = self.jira + f'project/{project_key}/role/{role}'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps({
            "group": [
                group
            ]
        })

        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def get_project_properties(self, project_key):
        url = self.jira + f"project/{project_key}/properties"

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def set_project_properties(self, project_key, property_key):
        data = json.dumps(property_key, sort_keys=True)
        url = self.jira + f"project/{project_key}/properties/{property_key}"

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            data=data,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def get_all_components(self, project_key):
        url = self.jira + f'project/{project_key}/components'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def move_components(self, payload):
        url = self.jira + 'component'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(payload)

        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        return response
