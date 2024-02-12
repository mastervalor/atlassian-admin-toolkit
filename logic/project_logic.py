from call import Jira
import json


class Projects:
    def __init__(self):
        self.jira = Jira()
        self.project_roles = {'Administrators': '10002', 'Developers': '10001', 'users': '10000', 'agents': '10301',
                              'customers': '10300'}

    def get_project_users_by_role(self, key, role):
        role_id = self.project_roles[role]
        users = self.jira.get_project_groups(key, role_id)
        groups = self.jira.get_project_groups(key, role_id)
        admins = []
        try:
            for user in users['actors']:
                if user['type'] == 'atlassian-user-role-actor':
                    admins.append(user['name'])

        except KeyError:
            print(f"the project {key} doesn't have any user in the {role} role")

        try:
            for group in groups['actors']:
                if group['type'] == 'atlassian-group-role-actor':
                    if group['name'] == 'Cruise Engineering':
                        print(f"There is an admins group in {key} called {group['name']}")
                    else:
                        members = self.jira.group_members(group['name'])
                        for member in members:
                            if member not in admins:
                                admins.append(member)

        except KeyError:
            print(f"the project {key} doesn't have any groups in the {role} role")

        return admins

    def get_project_type(self, key):
        project = self.jira.get_project(key)
        return project['projectTypeKey']