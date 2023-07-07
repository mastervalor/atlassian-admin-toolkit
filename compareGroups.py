import csv
import os
from call import Jira

jira = Jira()

newFile = 'members not in app-jira'

app_members = jira.group_members('app-jira')
jira_members = jira.group_members('jira-users')
jira_only = list(set(jira_members) - set(app_members))

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['usename'])
    for member in jira_only:
        writer.writerow([member])
        print(member)
