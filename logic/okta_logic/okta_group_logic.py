from logic.okta_logic.okta_user_logic import OktaUsers
from calls.okta_api_calls.okta_group_api import OktaGroupCalls


class OktaGroups:

    @classmethod
    def compare_users_groups(cls, user1, user2):
        user1_id = OktaUsers.get_user_id(user1)
        user2_id = OktaUsers.get_user_id(user2)
        user1_groups = set(OktaUsers.user_groups(user1_id))
        user2_groups = set(OktaUsers.user_groups(user2_id))

        return user1_groups.difference(user2_groups)

    @classmethod
    def add_user_to_groups(cls, user, groups):
        user_id = OktaUsers.get_user_id(user)
        for group in groups:
            group_id = OktaGroupCalls.get_group_id(group)
            if "Failed to retrieve group ID" in group_id or "Group not found" in group_id:
                print(f"Error: {group_id} for group: {group}. Skipping...")
                continue
            result = OktaGroupCalls.add_user_to_group(user_id, group_id)
            print(f'User: {user} being added to group: {group} got result code: {result}')

    @classmethod
    def get_group_users_by_name(cls, name):
        group_id = OktaGroupCalls.get_group_id(name)
        group_users = OktaGroupCalls.get_group_users(group_id)
        return group_users
