from calls.confluence_api_calls.conf_api_users import ConfluenceUsersCalls


class ConfGroupLogic:
    def __init__(self, is_staging=False):
        self.conf_users = ConfluenceUsersCalls(is_staging=True) if is_staging else ConfluenceUsersCalls()
