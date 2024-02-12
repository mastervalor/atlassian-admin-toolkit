import os
import csv
from logic.ticket_logic import Tickets

tickets = Tickets()
openFile = 'Project'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        ticket_info = {'parent ticket': 'CORPENG-8268'}
        ticket_info['summary'] = f"The project {i['Project Key']} needs to be rolled over to new standards"
        ticket_info['assignee'] = ""
        ticket_info['description'] = (f"The project {i['Project Key']} needs to be rolled over to new standards,"
                                      f" the owner of the project is {i['Owner']} and the project is a {i['Type']}"
                                      f" type.")

        tickets.build_ticket_payload(ticket_info)