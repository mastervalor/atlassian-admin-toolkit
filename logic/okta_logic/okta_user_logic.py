from calls.okta import Okta


class OktaUsers:

    def __init__(self):
        self.okta = Okta()

    @classmethod
    def get_user_manager(cls, email):
        user_profile = cls.user_id(email)
        manager = user_profile['profile']['manager']

        return manager

    @classmethod
    def get_user_status(cls,email):
        user_profile = cls.user_id(email)
        user_status = user_profile['status']

        return user_status