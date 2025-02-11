from calls.confluence_api_calls.conf_api_groups import ConfluenceGroupsCalls


class ConfGroupLogic:
    def __init__(self, is_staging=False):
        self.conf_groups = ConfluenceGroupsCalls(is_staging=True) if is_staging else ConfluenceGroupsCalls()

    def get_group_members(self, name):
        pref = f''
        members = self.conf_groups.group_members(name)



    def get_group_members_with_status(self, name):


