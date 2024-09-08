from logic.jira_logic.project_logic import Projects
from logic.os_logic.os_logic import OSLogic
import csv
import os
import urllib.parse

projects = Projects()
res = 'Priorities copy'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), res), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        encoded = urllib.parse.quote(i['Name'])
        results = call(f'priority="{encoded}"', 'search')
        try:
            i['Tickets'] = results['total']
            rows.append(i)
            print(i)
        except KeyError:
            print(i['Name'])
            rows.append(i)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()