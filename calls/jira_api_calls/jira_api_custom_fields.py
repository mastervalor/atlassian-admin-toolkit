import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class CustomFieldsJiraCalls:
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
