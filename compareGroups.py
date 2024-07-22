from logic.jira_logic.groups_users_logic import GroupsUsers
from logic.user_logic import Users
from logic.os_logic import OSLogic

groups = GroupsUsers()
users = Users()

newFile = 'members not in app-jira'
os_logic = OSLogic(write_file=newFile)

main_group = 'app-jira'
groups_list = ['administrators', 'app-jira-access', 'app-jira-contractor-users', 'Cruise Employees', 'Drives Services',
               'employees', 'engineering', 'GM Employees - Jira', 'jira-administrators', 'jira-users']
missing_members = []

for group in groups_list:
    members = groups.compare_groups(main_group, group)
    print(f"group {group} has these members missing: {members}")
    for member in members:
        if member not in missing_members:
            missing_members.append({'member': member, 'group': group})

print(missing_members)
data_to_write = [{'usename': member['member'], 'group': member['group'],
                  'status': users.get_user_status(member['member'])} for member in missing_members]

os_logic.write_to_file(data_to_write)
