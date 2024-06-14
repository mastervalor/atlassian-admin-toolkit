from calls.jira import Jira
import json


class Projects:
    def __init__(self, is_staging=False):
        self.jira = Jira(is_staging)
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

    def get_archived_projects(self):
        archived_projects = []
        projects = self.jira.get_projects_with_archived()
        for project in projects:
            if project['archived']:
                archived_projects.append(project)

        return archived_projects

    def get_project_owners_and_status(self):
        project_owners = []
        projects = self.jira.get_projects_with_owners()
        for project in projects:
            project_owners.append({
                'Project': project['name'],
                'Key': project['key'],
                'Name': project['lead']['displayName'],
                'Active': project['lead']['active']
            })

        return project_owners

    def change_issue_type_scheme(self, key, scheme):
        keys = key if isinstance(key, list) else [key]

        response = self.jira.post_issue_type_scheme(scheme, keys)

        return response

    def unarchive_projects_list(self, keys):
        responses = {}

        for key in keys:
            responses[key] = self.jira.unarchive_project(key)

        return responses

    def archive_projects_list(self, keys):
        responses = {}

        for key in keys:
            responses[key] = self.jira.archive_project(key)

        return responses
