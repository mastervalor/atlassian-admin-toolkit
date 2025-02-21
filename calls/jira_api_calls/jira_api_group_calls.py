import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class GroupJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

    def remove_group_member(self, group, user):
        url = self.jira + 'group/user'

        query = {
            'groupname': group,
            'username': user
        }

        response = requests.request(
            "DELETE",
            url,
            params=query,
            auth=self.token
        )

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

    def get_groups(self, starting, ending):
        url = self.jira + f'group/bulk?mstart={starting}&limit={ending}'

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

    def add_member_to_group(self, group, user):
        url = self.jira + f'group/user'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        query = {
            'groupname': group
        }

        payload = json.dumps({
            "accountId": user
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            params=query,
            auth=auth
        )

        return response
