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

    for name in reader:
        encoded = urllib.parse.quote(name['Name'])
        results = ticket_logic.get_tickets_from_jql(f'resolution="{encoded}"')
        try:
            name['Tickets'] = results['total']
            rows.append(name)
        except KeyError:
            rows.append(name)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()
