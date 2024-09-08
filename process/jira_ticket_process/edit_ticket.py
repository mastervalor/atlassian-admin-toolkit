from logic.jira_logic.ticket_logic import Tickets
from logic.os_logic.os_logic import OSLogic

tickets = Tickets()
os_logic = OSLogic(open_file='Design Intent Data')

file = os_logic.read_file()

for ticket in file:
    summary = ticket['Summary']
    jql = f'summary ~"{summary}" and project = "Behavior Requirements & Monitoring"'
    key = tickets.get_ticket_keys_from_jql(jql)[0]
    print(key)
