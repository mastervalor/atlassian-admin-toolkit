from calls.jira_api_calls.jira_api_group_calls import GroupJiraCalls
from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls
from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
from logic.jira_logic.group_logic import Groups
from logic.jira_logic.user_logic import Users
from logic.jira_logic.ticket_logic import Tickets


class Projects:
    def __init__(self, is_staging=False):
        self.jira_group_logic = Groups()
        self.jira_groups = GroupJiraCalls()
        self.jira_projects = ProjectJiraCalls()
        self.jira_tickets = TicketsJiraCalls()
        self.user_logic = Users()
        self.ticket_logic = Tickets()
        self.project_roles = {'Administrators': '10002', 'Developers': '10001', 'users': '10000', 'agents': '10301',
                              'customers': '10300'}

    def get_project_users_by_role(self, key, role):
        role_id = self.project_roles[role]
        users = self.jira_projects.get_project_groups(key, role_id)
        groups = self.jira_projects.get_project_groups(key, role_id)
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
                        members = self.jira_group_logic.group_members(group['name'])
                        for member in members:
                            if member not in admins:
                                admins.append(member)

        except KeyError:
            print(f"the project {key} doesn't have any groups in the {role} role")

        return admins

    def get_project_admins_group(self, key):
        role_id = self.project_roles['Administrators']
        groups = self.jira_projects.get_project_groups(key, role_id)
        for group in groups['actors']:
            if '-administrator' in group['displayName']:
                return group['displayName']

        return f"No administrator found in {key}"

    def get_project_users_group(self, key):
        role_id = self.project_roles['users']
        groups = self.jira_projects.get_project_groups(key, role_id)
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
        groups = self.jira_projects.get_project_groups(key, role_id)
        for group in groups['actors']:
            if '-agent' in group['displayName']:
                return group['displayName']

        return f"No agents found in {key}"

    def get_project_developers_group(self, key):
        role_id = self.project_roles['Developers']
        groups = self.jira_projects.get_project_groups(key, role_id)
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

        return project

    def get_archived_projects(self):
        archived_projects = []
        projects = self.jira_projects.get_projects_with_archived()
        for project in projects:
            if project['archived']:
                archived_projects.append(project)

        return archived_projects

    def get_active_all_project_keys(self):
        active_projects = []
        projects = self.jira_projects.get_projects()
        for project in projects:
            if project['key']:
                active_projects.append(project['key'])

        return active_projects

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

        response = self.jira_projects.post_issue_type_scheme(scheme, keys)

        return response

    def unarchive_projects_list(self, keys):
        responses = {}

        for key in keys:
            responses[key] = self.jira_projects.unarchive_project(key)

        return responses

    def archive_projects_list(self, keys):
        responses = {}

        for key in keys:
            responses[key] = self.jira_projects.archive_project(key)

        return responses

    def get_active_projects_total(self):
        projects = self.jira_projects.get_projects()
        number_of_projects = len(projects)
        return number_of_projects

    def get_active_projects(self):
        projects = self.jira_projects.get_projects()
        active_projects = []
        for project in projects:
            if (project['name'].startswith("[dead]") or project['name'].startswith("{Archived}")
                    or project['name'].startswith("{ARCHIVE}")
                    or ("archived" in project and project['archived'] == 'True')):
                continue
            else:
                active_projects.append(project)

        return active_projects

    def add_group_admins_to_project(self, group, project_key):
        response = self.jira_projects.add_group_by_role(group, '10002', project_key)
        return response

    def add_group_to_project_by_role(self, group, role, project_key):
        response = self.jira_projects.add_group_by_role(group, role, project_key)
        return response

    def get_project_properties(self, project_key):
        response = self.jira_projects.get_project_properties(project_key)
        if response.status_code != 200:
            print("Sorry that's not an exciting project key, please try again. Good bye")
            quit()
        else:
            return response

    def set_project_properties(self, project_key, property_key):
        response = self.jira_projects.set_project_properties(project_key, property_key)
        if response.status_code != 200:
            print("Sorry that's not an exciting project key, please try again. Good bye")
            quit()
        else:
            return response

    def get_project_owner(self, project_key):
        owner = self.jira_projects.project_owner(project_key)
        return owner[0]

    def get_owner_of_projects(self, project_list):
        project_owners = []

        for project in project_list:
            project_owners.append(self.jira_projects.project_owner(project))

        return project_owners

    def get_project_owner_with_status(self, project_key):
        owner = self.jira_projects.project_owner(project_key)
        return owner

    def get_project(self, project_key):
        project = self.jira_projects.get_project(project_key)
        return project

    def get_inactive_assignees_and_reporters_in_project(self, project_key):
        """
        Fetches all issues in a project with inactive assignees or reporters.

        :param project_key: Jira project key.
        :return: Two lists of inactive assignees and reporters.
        """
        payload = (f'project = {project_key} AND (assignee in inactiveUsers() OR reporter in inactiveUsers()) AND '
                   f'resolution is EMPTY')
        tickets = self.jira_tickets.jql('', payload)['issues']

        assignee_list = []
        reporter_list = []

        for ticket in tickets:
            issue_key = ticket['key']
            fields = ticket['fields']

            # Check Reporter
            if fields.get('reporter') and not fields['reporter']['active']:
                reporter = fields['reporter']
                reporter_list.append((issue_key, reporter['accountId']))

            # Check Assignee
            if fields.get('assignee') and not fields['assignee']['active']:
                assignee = fields['assignee']
                assignee_list.append((issue_key, assignee['accountId']))

        return assignee_list, reporter_list

    def reassign_inactive_users(self, project_key):
        """
        Reassigns inactive users (assignees and reporters) to their manager.

        :param project_key: Jira project key.
        """
        assignees, reporters = self.get_inactive_assignees_and_reporters_in_project(project_key)

        for issue_key, account_id in assignees:
            user_profile = self.user_logic.get_user_by_id(account_id)
            manager_id = user_profile.get('value', {}).get('manager')

            if manager_id:
                self.ticket_logic.assign_ticket(issue_key, manager_id)
            else:
                print(f"The Assignee in {issue_key} does not have a listed manager.")

        for issue_key, account_id in reporters:
            user_profile = self.user_logic.get_user_by_id(account_id)
            manager_id = user_profile.get('value', {}).get('manager')

            if manager_id:
                self.ticket_logic.assign_reporter_ticket(issue_key, manager_id)
            else:
                print(f"The Reporter in {issue_key} does not have a listed manager.")
