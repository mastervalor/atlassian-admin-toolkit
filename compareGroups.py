import csv
import os
from logic.groups_users_logic import GroupsUsers
from logic.user_logic import Users

groups = GroupsUsers()
users = Users()

newFile = 'members not in app-jira'

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

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['usename', 'group', 'status'])
    for member in missing_members:
        member_status = users.get_user_status(member)
        writer.writerow([member['member'], member['group'], member_status])
        print(member)


