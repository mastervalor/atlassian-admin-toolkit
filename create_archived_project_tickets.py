from logic.os_logic import OSLogic
from logic.ticket_logic import Tickets

os_logic = OSLogic(open_file='Archived projects')
file = os_logic.read_file()

for row in file:
    ticket_info = {'parent ticket': 'CORPENG-9593',
                   'summary': f"Project {row['project_key']} needs to be rolled over to new archived project standards",
                   'assignee': "msteam@praecipio.com"}

    print(row)
