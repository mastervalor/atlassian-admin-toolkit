from calls.jira_api_calls.jira_api_group_calls import GroupJiraCalls


class Groups:
    def __init__(self, is_staging=False):
        self.jira_groups = GroupJiraCalls(is_staging=True) if is_staging else GroupJiraCalls()

    def remove_default_admins(self, admins):
        sys_admins = self.group_members("administrators")
        final = []
        for admin in admins:
            if admin not in sys_admins and ".svc" not in admin and ".car" not in admin:
                final.append(admin)

        return final

    def get_group_members_with_status(self, group, inactive=False):
        start_at = 0
        max_results = 50
        total = 51
        members_list = []

        while total >= max_results:
            if inactive:
                members = self.jira_groups.get_group(f'?includeInactiveUsers=true&startAt={start_at}'
                                                     f'&maxResults={max_results}', group)
            else:
                members = self.jira_groups.get_group(f'?includeInactiveUsers=false&startAt={start_at}'
                                                     f'&maxResults={max_results}', group)

            try:
                for member in members['values']:
                    members_list.append(member['name'])

                total = members['total']
                start_at += 50
                max_results += 50
            except KeyError:
                return []

        return members_list

    def remove_all_group_members(self, group):
        members = self.get_group_members_with_status(group, True)

        for member in members:
            response = self.jira_groups.remove_group_member(group, member)
            print(response)

    def compare_groups(self, group1, group2):
        group_one = self.group_members(group1)
        group_two = self.group_members(group2)
        different_members = []

        for member in group_two:
            if member not in group_one:
                different_members.append(member)

        return different_members

    def group_members(self, group):
        start_at = 0
        max_results = 50
        total = 51
        members_list = []

        while total >= max_results:
            members = self.jira_groups.get_group(f'?includeInactiveUsers=false&startAt={start_at}'
                                                 f'&maxResults={max_results}', group)

            for member in members['values']:
                members_list.append(member['name'])

            total = members['total']
            start_at += 50
            max_results += 50
            # print(startAt, maxResults)
        return members_list

    def get_all_groups(self):
        min = 0
        max = 100
        total = 100
        groups = []
        while max <= total:
            response = get_groups(min, max)
            for i in response['values']:
                groups.append(i['name'])
            min += 100
            max += 100
            total = response['total']

        return groups
