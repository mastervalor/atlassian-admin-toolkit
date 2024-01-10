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

        if not i['Project admins']:
            admins = "No admins"
        else:
            admins = i['Project admins']

        if i['potential owner']:
            owner = i['potential owner']
        else:
            owner = "none found"

        if 'Vice' not in i['next_active_management_title'] and 'President' not in i['next_active_management_title']:
            ticket_info['description'] = (f"The project {i['Name']}: {i['Key']} has no owner and we need to find a new "
                                          f"owner for this project. If we have a potenial owner it would be: {owner}. "
                                          f"The next next manager of the formal project lead is "
                                          f"{i['next_active_management']}. The admins in the project are: {admins}")
        else:
            ticket_info['description'] = (f"The project {i['Name']}: {i['Key']} has no owner and we need to find a new "
                                          f"owner for this project. The next next manager is a VP so need to look for "
                                          f"approver else where. The admins in the project are: {admins}")

        tickets.build_ticket_payload(ticket_info)
