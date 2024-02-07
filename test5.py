from call import Jira
from logic.groups_users_logic import GroupsUsers

groups = GroupsUsers()

groups.remove_all_group_members("jira-new-hires")


# print(members, sort_keys=True, indent=4, separators=(",", ": "))