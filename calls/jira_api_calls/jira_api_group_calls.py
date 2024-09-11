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
        startAt = 0
        maxResults = 50
        total = 51
        members_list = []

        while total >= maxResults:
            members = self.jira_users.get_group(f'?includeInactiveUsers=false&startAt={startAt}'
                                                f'&maxResults={maxResults}', group)

            for member in members['values']:
                members_list.append(member['name'])

            total = members['total']
            startAt += 50
            maxResults += 50
            # print(startAt, maxResults)
        return members_list
