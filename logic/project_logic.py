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

        for group in groups['actors']:
            if group['type'] == 'atlassian-group-role-actor':
                print(group['name'])

        # print(json.dumps(groups, sort_keys=True, indent=4, separators=(",", ": ")))

    def get_project_users_by_role(self, key, role):
        role_id = self.project_roles[role]
        groups = self.jira.get_project_groups(key, role_id)

        for group in groups['actors']:
            if group['type'] == 'atlassian-user-role-actor':
                print(group['name'])


projects = Projects()
projects.get_project_users_by_role('ITAPP', 'Administrators')
