from calls.jira import Jira


class Users:
    def __init__(self, is_staging=False):
        self.jira = Jira(is_staging=True) if is_staging else Jira()

    def user_groups(self, user):
        groups = self.jira.get_user(user, '?expand=groups')
        user_groups = []

        for group in groups['groups']['items']:
            user_groups.append(group['name'])

        return user_groups

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
            roles.append(role['name'])

        return roles

    def delete_list_of_users(self, user):
