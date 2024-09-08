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










# tickets = jira.jql('?startAt=0&maxResults=1000', 'project = "IT Apps" and "Level of Effort" = "Strategic Work" and '
#                                                  'summary ~ "Project does not meet the new requirments"')
# for ticket in tickets['issues']:
#     if "requirments" in ticket['fields']['summary']:
#         corrected_summary = ticket['fields']['summary'].replace("requirments", "requirements", 1)
#         corrected_description = ticket['fields']['description'].replace("Do to this this", "Due to this", 1)
#         payload = {
#             "fields": {
#                 'summary': corrected_summary,
#                 'description': corrected_description
#             }
#         }
#         correct = jira.edit_ticket(ticket['key'], payload)
#         print(ticket['key'] + "corrected")
#     else:
#         print(ticket['key'] + "doesn't need correction")