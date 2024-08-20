from calls.okta import Okta

class OktaGroups:

    @classmethod
    def compare_users_groups(cls, user1, user2):
        user1_id = Okta.users_id(user1)
        user2_id = Okta.users_id(user2)
        user1_groups = Okta.get_user_groups(user1_id)
        user2_groups = Okta.get_user_groups(user2_id)