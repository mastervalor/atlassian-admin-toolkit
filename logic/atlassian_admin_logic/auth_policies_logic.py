from calls.atlassian_admin_api_calls.auth_policies_api import AtlassianAuthPolicies


class AuthPolicies:
    def __init__(self):
        self.auth_policies = AtlassianAuthPolicies()

    def get_status_of_task(self, task_id):
        response = self.auth_policies.get_task_status(task_id)

    def add_users_to_auth_policies(self, users, policy_id):
        user_responses = []
        for user in users:
            response = self.auth_policies.add_user_to_policy(user, policy_id)
            user_responses.append({
                'user': user,
                'task_id': response['taskId'],
                'task_link': response['taskLink']
            })
