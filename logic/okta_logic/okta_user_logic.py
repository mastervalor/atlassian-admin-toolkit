from calls.okta import Okta


class OktaUsers:

    def __init__(self):
        self.okta = Okta()

    @classmethod
    def get_user_manager(cls, email):
        user_profile = cls.user_id(email)
        manager = user_profile['profile']['manager']

        return manager