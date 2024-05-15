from calls.jira import Jira


class Users:
    def __init__(self):
        self.jira = Jira()

    def user_groups(self, user):
        groups = self.jira.get_user(user, '?expand=groups')
        user_groups = []

        for group in groups['groups']['items']:
            user_groups.append(group['name'])

        return user_groups
