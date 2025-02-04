import csv
import os
from logic.jira_logic.group_logic import Groups

admins = 'Jira admins copy'
groups = Groups()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), admins), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        response = groups.group_members(i["Group Name"])
        i['Members'] = response['total']
        rows.append(i)
        print(i)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()
