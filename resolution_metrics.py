import csv
import os
import urllib.parse
from logic.jira_logic.ticket_logic import Tickets

res = 'Resolutions - Sheet copy'
ticket_logic = Tickets()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), res), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        encoded = urllib.parse.quote(i['Name'])
        results = ticket_logic.get_tickets_from_jql(f'resolution="{encoded}"')
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
