from logic.jira_logic.group_logic import Groups
import csv
import os

jira_groups = Groups()
newFile = "app-jira members"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username'])
    response = jira_groups.group_members('app-jira')
    for member in response:
        writer.writerow([member])
        print(member)
