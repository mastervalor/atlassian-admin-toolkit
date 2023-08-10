import json
import csv
import os
from call import Jira

jira = Jira()
newFile = "app-jira members"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username'])
    response = jira.group_members('app-jira')
    for member in response:
        writer.writerow([member])
        print(member)
