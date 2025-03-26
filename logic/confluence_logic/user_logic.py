from calls.confluence_api_calls.conf_api_users import ConfluenceUsersCalls


class ConfUserLogic:
    def __init__(self, is_staging=False):
        self.conf_users = ConfluenceUsersCalls(is_staging=True) if is_staging else ConfluenceUsersCalls()

    def get_users_groups(self, username):
        users_groups = self.conf_users.user_groups(username)
        return users_groups
    