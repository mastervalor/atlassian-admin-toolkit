import requests
from auth import atlassian_admin_Bearer_token
import json
from config import atlassian_admin_v1


class AtlassianAuthPolicies:
    def __init__(self):
        self.token = atlassian_admin_Bearer_token
        self.admin_url = atlassian_admin_v1
        self.org_id = 'd816j2aj-j881-10a8-7c2c-10c7736ca181'

    def add_user_to_policy(self, user, policy_id):
        url = self.admin_url + f"orgs/{self.org_id}/auth-policy/{policy_id}/add-users"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.token
        }

        payload = json.dumps({
            "users": [
                user
            ]
        })

        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers
        ).text)

        return response

    def get_task_status(self, task_id):
        url = self.admin_url + f"orgs/{self.org_id}/auth-policy/task/{task_id}"

        headers = {
            "Accept": "application/json",
            "Authorization": self.token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers
        )

        return response
    