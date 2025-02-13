from calls.confluence_api_calls.conf_api_groups import ConfluenceGroupsCalls


class ConfGroupLogic:
    def __init__(self, is_staging=False):
        self.conf_groups = ConfluenceGroupsCalls(is_staging=True) if is_staging else ConfluenceGroupsCalls()

    def get_group_members(self, name):
        members = self.conf_groups.group_members(name)
        return members

    def get_group_members_with_status(self, name, expanded):
        members_with_status = self.conf_groups.group_members(name, expanded)
        return members_with_status

    def get_group_users_email(self, group):
        start_at = 0
        max_results = 50
        total = 51
        members_list = []
        try:
            self.conf_groups.get_group(f'?startAt={start_at}&maxResults={max_results}', group)
            while total >= max_results:
                response = self.conf_groups.get_group(f'?startAt={start_at}&maxResults={max_results}', group)
                if group != 'administrators':
                    for i in response['values']:
                        try:
                            members_list.append(i['emailAddress'])
                        except KeyError:
                            print(f'User Id {i["accountId"]} was not caught in the group grab')
                    start_at += 50
                    max_results += 50
                    total = response['total']
        except KeyError:
            print(f"This group {group} doesn't exist")

        return members_list
