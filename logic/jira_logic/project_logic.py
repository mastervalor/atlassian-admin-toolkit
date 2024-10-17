from calls.jira import Jira
from calls.jira_api_calls.jira_api_group_calls import GroupJiraCalls
from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls


class Projects:
    def __init__(self, is_staging=False):
        self.jira = Jira(is_staging)
        self.jira_groups = GroupJiraCalls()
        self.jira_projects = ProjectJiraCalls()
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
                        members = self.jira_groups.group_members(group['name'])
                        for member in members:
                            if member not in admins:
                                admins.append(member)

        except KeyError:
            print(f"the project {key} doesn't have any groups in the {role} role")

        return admins

    def get_project_admins_group(self, key):
        role_id = self.project_roles['Administrators']
        groups = self.jira.get_project_groups(key, role_id)
        for group in groups['actors']:
            if '-administrator' in group['displayName']:
                return group['displayName']

        return f"No administrator found in {key}"

    def get_project_users_group(self, key):
        role_id = self.project_roles['users']
        groups = self.jira.get_project_groups(key, role_id)
        standard_group = ''
        for group in groups['actors']:
            if '-user' in group['displayName']:
                if group['displayName'] == 'jira-users':
                    standard_group = group['displayName']
                else:
                    return group['displayName']

        if standard_group == 'jira-users':
            return standard_group

        return f"No users found in {key}"

    def get_project_agents_group(self, key):
        role_id = self.project_roles['agents']
        groups = self.jira.get_project_groups(key, role_id)
        for group in groups['actors']:
            if '-agent' in group['displayName']:
                return group['displayName']

        return f"No agents found in {key}"

    def get_project_developers_group(self, key):
        role_id = self.project_roles['Developers']
        groups = self.jira.get_project_groups(key, role_id)
        standard_group = ''
        for group in groups['actors']:
            if '-developer' in group['displayName']:
                if group['displayName'] == 'jira-developers':
                    standard_group = group['displayName']
                else:
                    return group['displayName']

        if standard_group == 'jira-developers':
            return standard_group

        return f"No developer found in {key}"

    def get_project_type(self, key):
        project = self.jira_projects.get_project(key)
        return project['projectTypeKey']

    def build_project_table(self, name, key, approver, approver_status):
        project = {
            'Name': name,
            'Key': key,
            'Approver': approver,
            'Approver status': approver_status,
            'Admin group': self.get_project_admins_group(key),
            'Developer group': self.get_project_developers_group(key),
            'User group': self.get_project_users_group(key),
            'Agent group': self.get_project_agents_group(key),
            'Project type': self.get_project_type(key)
        }

        print(project)
        return project

    def get_archived_projects(self):
        archived_projects = []
        projects = self.jira.get_projects_with_archived()
        for project in projects:
            if project['archived']:
                archived_projects.append(project)

        return archived_projects

    def get_project_owners_and_status(self):
        project_owners = []
        projects = self.jira_projects.get_projects_with_owners()
        for project in projects:
            project_owners.append({
                'Project': project['name'],
                'Key': project['key'],
                'Name': project['lead']['displayName'],
                'Username': project['lead']['name'],
                'Active': project['lead']['active'],
                'Project_archived': project['archived'],
                'Type': project['projectTypeKey']
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

    def get_active_projects_total(self):
        projects = self.jira.get_active_projects()
        number_of_projects = len(projects)
        return number_of_projects
