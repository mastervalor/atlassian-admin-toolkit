from logic.jira_logic.ticket_logic import Tickets
from logic.jira_logic.project_logic import Projects
import re
import os
import csv


def extract_section(input_string):
    match = re.search(r':\s(\w+)', input_string)
    if match:
        return match.group(1)
    else:
        return None


ticket_logic = Tickets()
project_logic = Projects()
newFile = 'project status'
openFile = 'all projects'

tickets = ticket_logic.get_tickets_from_jql('project = "IT Apps" and "Level of Effort" = "Strategic Work" '
                                            'and summary ~ "does not meet the new requirements,"')
with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'key', 'Project Type', 'Project Id', 'Total Tickets', 'Last ticket',
                     'Last ticket creation date', 'Earliest ticket', 'Earliest ticket creation date',
                     'project Owner', 'project owner status', 'Approver', 'Owner approved', 'Project status',
                     'Ticket number', 'Ticket status', 'Ticket assignee', 'Notes'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_rows = list(csv_reader)
        for i in tickets['issues']:
            key = extract_section(i['fields']['description'])
            for j in csv_rows:
                if key == j['key']:
                    try:
                        approver = i['fields']['customfield_13230'][0]['displayName']
                    except TypeError:
                        approver = "no approver"
                    owner, owner_status = project_logic.get_project_owner_with_status(key)
                    assignee = i['fields']['assignee']['name']
                    try:
                        status = jira.get_project(key)['archived']
                    except KeyError:
                        status = True
                    if status:
                        status = "archived"
                    else:
                        status = "active"
                    ticket_status = i['fields']['status']['name']
                    try:
                        res = i['fields']['resolution']['name']
                    except TypeError:
                        res = None

                    if res == 'Cancelled':
                        note = 'Exception was made'

                    if status == 'Backlog':
                        note = 'Looking for owner'
                    elif status == 'On Hold':
                        note = 'project will me consolidated'
                    elif status == 'Waiting for Response':
                        note = 'Waiting for approval from owner'
                    elif status == 'In Progress':
                        note = 'Approved ready for archive'
                    else:
                        note = ''

                    print(j['key'], i['key'], owner, approver, status, ticket_status, assignee, note)
                    writer.writerow([j['Name'], j['key'], j['Project Type'], j['Project Id'], j['Total Tickets'],
                                    j['Last ticket'], j['Last ticket creation date'], j['Earliest ticket'],
                                    j['Earliest ticket creation date'], owner, owner_status, approver, '', status,
                                     i['key'], ticket_status, assignee, note])


# print(json.dumps(tickets, sort_keys=True, indent=4, separators=(",", ": ")))
