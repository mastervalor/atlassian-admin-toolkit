from calls.jira import Jira
import json


class GroupsUsers:
    def __init__(self):
        self.jira = Jira()

    def remove_defult_admins(self, admins):
        sys_admins = self.jira.group_members("administrators")
        final = []
        for admin in admins:
            if admin not in sys_admins and ".svc" not in admin and ".car" not in admin:
                final.append(admin)

        return final

    def get_group_members_with_status(self, group, inactive=False):
        startAt = 0
        maxResults = 50
        total = 51
        members_list = []

        while total >= maxResults:
            if inactive:
                members = self.jira.get_group(f'?includeInactiveUsers=true&startAt={startAt}'
                                              f'&maxResults={maxResults}', group)
            else:
                members = self.jira.get_group(f'?includeInactiveUsers=false&startAt={startAt}'
                                              f'&maxResults={maxResults}', group)

            try:
                for member in members['values']:
                    members_list.append(member['name'])

                total = members['total']
                startAt += 50
                maxResults += 50
                # print(startAt, maxResults)
            except KeyError:
                return []

        return members_list

    def remove_all_group_members(self, group):
        members = self.get_group_members_with_status(group, True)

        for member in members:
            response = self.jira.remove_group_member(group, member)
            print(response)

    def user_groups(self, user):
        groups = self.jira.get_user(user, '?expand=groups')
        user_groups = []

        for group in groups['groups']['items']:
            user_groups.append(group['name'])

        return user_groups

    def compare_groups(self, group1, group2):
        group_one = self.jira.group_members(group1)
        group_two = self.jira.group_members(group2)
        different_members = []

        for member in group_two:
            if member not in group_one:
                different_members.append(member)

        return different_members

    def get_user_status(self, user):
        user_profile = self.jira.get_user(user)
        if user_profile['active']:
            return 'Active'
        else:
            return 'Inactive'

    def get_user_applications(self, user):
        user_profile = self.jira.get_user(user, '?expand=applicationRoles')
        roles = []
        for role in user_profile['applicationRoles']['items']:
            print(role['name'])