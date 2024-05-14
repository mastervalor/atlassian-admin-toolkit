import csv
import os
from logic.groups_users_logic import GroupsUsers

groups = GroupsUsers()

newFile = 'members not in app-jira'

main_group = 'app-jira'
groups = ['administrators', 'app-jira-access', 'app-jira-contractor-users', 'Cruise Employees', 'Drives Services',
          'employees', 'engineering', 'GM Employees - Jira', 'jira-administrators', 'jira-users']


with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['usename', 'group', 'status', 'directory'])
    for member in jira_only:
        writer.writerow([member])
        print(member)
