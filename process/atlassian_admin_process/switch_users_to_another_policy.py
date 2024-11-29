from file_manip.csv_file_manip import CSVLogic
from logic.atlassian_admin_logic.auth_policies_logic import AuthPolicies


csv_logic = CSVLogic(open_file='old_policy_members')
old_policy = csv_logic.read_file()
auth_policies = AuthPolicies()
new_policy = "3b93d6bc-1087-427f-b1a9-0dacc7bb837f"
users = []

# auth_policies.get_status_of_task('3388a70e-1fb5-42cb-868e-335e7681331e')
for user in old_policy:
    users.append(user['Email'])

auth_policies.add_users_to_auth_policies(users, new_policy)
