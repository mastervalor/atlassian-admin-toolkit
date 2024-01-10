import os
import csv
from logic.ticket_logic import Tickets

tickets = Tickets()
openFile = 'unowned projects'
assingees = {"mourad.marzouk": 0, "justin.che": 0, "oscar.h.singson": 0}

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        ticket_info = {'parent ticket': 'ITAPP-7856'}
        ticket_info['summary'] = f"The project {i['Name']}: {i['Key']} has no owner"

        if i['potential owner'] == "Mourad Marzouk":
            ticket_info['assignee'] = "mourad.marzouk"
            assingees['mourad.marzouk'] += 1
        else:
            lowest_assignee = min(assingees, key=assingees.get)
            ticket_info['assignee'] = lowest_assignee
            assingees[lowest_assignee] += 1

        if i['Project admins']:
            admins = i['Project admins']
        else:
            admins = None

        if i['potential owner']:
            ticket_info['approver'] = i['potential owner']
        else:
            ticket_info['approver'] = ''

        if 'Vice' not in i['next_active_management_title'] and 'President' not in i['next_active_management_title']:
            ticket_info['description'] = (f"The project {i['Name']}: {i['Key']} has no owner and we need to find a new "
                                          f"owner for this project. The next next manager "
                                          f"of the formal project lead is {i['next_active_management']}. The admins "
                                          f"In the project are: {admins}")

        tickets.build_ticket_payload(ticket_info)
