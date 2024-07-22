from logic.os_logic import OSLogic
from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()
os_logic = OSLogic(open_file='Archived projects')
file = os_logic.read_file()

for row in file:
    ticket_info = {'parent ticket': 'CORPENG-9593',
                   'summary': f"Project {row['project_key']} needs to be rolled over to new archived project standards",
                   'assignee': "msteam@praecipio.com",
                   'description': (f"Project {row['project_key']} needs to be rolled over to new archived project "
                                   f"standards, the project will need to be unarchived, then follow these steps to roll"
                                   f" over to new standards: https://wiki.robot.car/display/IT/%5BInternal%5D+Jira+Clean+up+Phase+1+Archiving+Projects+Runbook"
                                   f". Then re-archive the project")}

    tickets.build_ticket_payload(ticket_info)
