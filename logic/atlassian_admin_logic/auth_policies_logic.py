from calls.atlassian_admin_api_calls.auth_policies_api import AtlassianAuthPolicies


class AuthPolicies:
    def __init__(self):
        self.auth_policies = AtlassianAuthPolicies()

    def add_users_to_auth_policies(self, users, policy_id):
        for user in users:
            self.auth_policies.add_user_to_policy(user, policy_id)
