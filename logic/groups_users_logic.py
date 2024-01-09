from call import Jira
import json

class Groups_users:
    def __init__(self):
        self.jira = Jira()

    def remove_defult_admins(self, admins):
        sys_admins = self.jira.group_members("administrators")
        final = []
        for admin in admins:
            if admin not in sys_admins and ".svc" not in admin and ".car" not in admin:
                final.append(admin)

        return final