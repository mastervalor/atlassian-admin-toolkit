import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class Jira:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

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
