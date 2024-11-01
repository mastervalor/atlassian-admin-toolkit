from calls.okta_api_calls.okta_users_api import OktaUsersCalls


class OktaUsers:

    @classmethod
    def get_user_manager(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        try:
            manager = user_profile['profile']['manager']
            return manager
        except KeyError:
            print(f'no manager found for: {email}')
            return None
        except TypeError:
            print(f'only found: {user_profile}')
            return None

    @classmethod
    def get_user_id(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        try:
            manager = user_profile['id']
            return manager
        except KeyError:
            print(f'no id found for: {email}')
            return None

    @classmethod
    def get_user_status(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        if user_profile:
            return user_profile['status']
        else:
            return None

    @classmethod
    def get_user_title(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        try:
            user_title = user_profile['profile']['title']
        except TypeError:
            print(f'only found: {user_profile}')
            return None
        return user_title

    @classmethod
    def get_user_second_email(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        try:
            second_email = user_profile['profile']['secondEmail']
            return second_email
        except TypeError:
            return None

    @classmethod
    def get_manager_info(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        manager = cls.get_user_manager(email)
        if manager is None:
            return "None", "None", "None"
        manager_title = cls.get_user_title(manager)
        manager_status = cls.get_user_status(manager)

        return manager, manager_title, manager_status

    @classmethod
    def get_user_email(cls, email):
        if "@" not in email:
            email = email + '@getcruise.com'
        user_profile = OktaUsersCalls.users_profile(email)
        if user_profile:
            return user_profile['profile']['email']
        else:
            return None
