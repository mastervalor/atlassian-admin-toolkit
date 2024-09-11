import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class UserJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

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

    def delete_user(self, username):
        url = self.jira + 'user'

        query = {
            'username': username
        }

        response = requests.request(
            "DELETE",
            url,
            params=query,
            auth=self.token
        ).text

        return response

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
    