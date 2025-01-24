import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class ProjectJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

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

    def get_projects_with_owners(self):
        url = self.jira + 'project?expand=lead'

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

    def get_active_projects(self):
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
