from logic.jira_logic.project_logic import Projects
from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
from file_manip.csv_file_manip import CSVLogic
import csv
import os
import urllib.parse

projects = Projects()
tickets = TicketsJiraCalls()
csv_logic = CSVLogic()
res = 'Priorities copy'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), res), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        encoded = urllib.parse.quote(i['Name'])
        results = tickets.jql(f'priority="{encoded}"', 'search')
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
