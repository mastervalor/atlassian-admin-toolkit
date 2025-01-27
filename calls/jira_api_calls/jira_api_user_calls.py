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

    def get_user_by_key(self, payload, pref=''):
        url = self.jira + 'user' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': payload,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

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

