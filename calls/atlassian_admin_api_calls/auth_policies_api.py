import requests
from auth import atlassian_admin_Bearer_token
import json
from config import atlassian_admin_v1


class AtlassianAuthPolicies:
    def __init__(self):
        self.token = atlassian_admin_Bearer_token
        self.admin_url = atlassian_admin_v1

    def add_user_to_policy(self, user, policy_id):
        org_id = 'd816j2aj-j881-10a8-7c2c-10c7736ca181'
        url = f"orgs/{org_id}/auth-policy/{policy_id}/add-users"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": atlassian_admin_Bearer_token
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
