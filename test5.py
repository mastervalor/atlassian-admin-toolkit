from logic.groups_users_logic import GroupsUsers

groups = GroupsUsers()

members = groups.get_group_members_with_status("jira-new-hires", True)

for i in members:
    print(i)