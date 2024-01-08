from call import Jira
import json


class Projects:
    def __init__(self):
        self.jira = Jira()
        self.project_roles = {'Administrators': '10002', 'Developers': '10001', 'users': '10000', 'agents': '10301',
                              'customers': '10300'}

    def get_project_groups_by_role(self, key, role):
        role_id = self.project_roles[role]
        groups = self.jira.get_project_groups(key, role_id)
        admins = []
        for group in groups['actors']:
            if group['type'] == 'atlassian-group-role-actor':
                admins.append(group['name'])

        return admins

        # print(json.dumps(groups, sort_keys=True, indent=4, separators=(",", ": ")))

    def get_project_users_by_role(self, key, role):
        role_id = self.project_roles[role]
        users = self.jira.get_project_groups(key, role_id)
        admins = []
        for user in users['actors']:
            if user['type'] == 'atlassian-user-role-actor':
                admins.append(user['name'])

        return admins


projects = Projects()
# projects.get_project_users_by_role('ITAPP', 'Administrators')
list = projects.get_project_users_by_role('ITAPP', 'Administrators')

print(list)
