import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging
from calls.jira_api_calls.jira_api_user_calls import UserJiraCalls


class GroupJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira
        self.jira_users = UserJiraCalls()

    def group_members(self, group):
        start_at = 0
        max_results = 50
        total = 51
        members_list = []

        while total >= max_results:
            members = self.jira_users.get_group(f'?includeInactiveUsers=false&startAt={start_at}'
                                                f'&maxResults={max_results}', group)

            for member in members['values']:
                members_list.append(member['name'])

            total = members['total']
            start_at += 50
            max_results += 50
            # print(startAt, maxResults)
        return members_list

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
        ).text

        return response
