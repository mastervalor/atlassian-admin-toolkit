from logic.os_logic.os_logic import OSLogic
from logic.atlassian_admin_logic.auth_policies_logic import AuthPolicies


os_logic = OSLogic(open_file='old_policy_members')
old_policy = os_logic.read_file()
auth_policies = AuthPolicies()
new_policy = "3b93d6bc-1087-427f-b1a9-0dacc7bb837f"
users = []

for user in old_policy:
    users.append(user['Email'])

# auth_policies.add_users_to_auth_policies(users, new_policy)

auth_policies.add_users_to_auth_policies(['vernie.del.mundo@getcruise.com'], new_policy)
