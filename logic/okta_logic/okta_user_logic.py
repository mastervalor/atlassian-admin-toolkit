from calls.okta import Okta


class OktaUsers:

    @classmethod
    def get_user_manager(cls, email):
        if "@getcruise.com" not in email:
            email = email + '@getcruise.com'
        user_profile = Okta.users_id(email)
        try:
            manager = user_profile['profile']['manager']
            return manager
        except KeyError:
            print(f'no manager found for: {email}')
            return "None"

    @classmethod
    def get_user_status(cls, email):
        if "@getcruise.com" not in email:
            email = email + '@getcruise.com'
        user_profile = Okta.users_id(email)
        user_status = user_profile['status']
        return user_status

    @classmethod
    def get_user_title(cls, email):
        if "@getcruise.com" not in email:
            email = email + '@getcruise.com'
        user_profile = Okta.users_id(email)
        user_title = user_profile['profile']['title']
        return user_title

    @classmethod
    def get_manager_info(cls, email):
        if "@getcruise.com" not in email:
            email = email + '@getcruise.com'
        manager = cls.get_user_manager(email)
        manager_title = cls.get_user_title(manager)
        manager_status = cls.get_user_status(manager)

        return manager, manager_title, manager_status
