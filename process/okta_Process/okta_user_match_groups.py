from logic.okta_logic.okta_group_logic import OktaGroups

user1 = 'satchidanand.challapalli@getcruise.com'
user2 = 'sumaiah.syed@getcruise.com'

compared_groups = OktaGroups.compare_users_groups(user1, user2)
print(compared_groups)
