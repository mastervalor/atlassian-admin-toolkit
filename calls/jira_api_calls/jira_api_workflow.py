import requests
from requests.auth import HTTPBasicAuth
from auth import auth, staging_auth, email
import json
from config import jira, jira_staging, jira_agile, jira_agile_dev


class WorkflowJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira_agile = jira_agile_dev if is_staging else jira_agile
        self.jira = jira_staging if is_staging else jira
        self.auth = HTTPBasicAuth(email, self.token)

    def get_workflows(self):
        url = self.jira + "workflow"

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

    def delete_workflow(self, workflow_id):
        url = self.jira + f"workflow/{workflow_id}"

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "DELETE",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def get_workflow_by_name(self, workflow_name):
        url = self.jira + f'workflow/search?workflowName={workflow_name}'
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
