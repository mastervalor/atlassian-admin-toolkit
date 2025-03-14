from call import call
from logic.jira_logic.system_logic import JiraSystemsLogic
from logic.jira_logic.ticket_logic import Tickets
import csv
import os
import urllib.parse

page = "issue types"
jira_system = JiraSystemsLogic()
ticket_logic = Tickets()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), page), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'Ticket count'])
    results = jira_system.get_all_issue_types()
    for i in results:
        encoded = urllib.parse.quote(i['name'])
        search = call(f'issuetype="{encoded}"', 'search')
        try:
            total = search['total']
            print(i['name'], total)
            writer.writerow([i['name'], total])
        except KeyError:
            print(i['name'])
            writer.writerow([i['name'], 'Sub-Task', 0])

# print(json.dumps(results, sort_keys=True, indent=4, separators=(",", ": ")))