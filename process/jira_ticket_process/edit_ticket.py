from logic.jira_logic.ticket_logic import Tickets
from file_manip.csv_file_manip import CSVLogic

tickets = Tickets()
csv_logic = CSVLogic(open_file='Design Intent Data')

file = csv_logic.read_file()

for ticket in file:
    summary = ticket['Summary']
    if '[Guidance]' in summary:
        summary = summary.replace("[Guidance]", "")
    jql = f'summary ~"{summary}" and project = "Behavior Requirements & Monitoring"'
    key = tickets.get_ticket_keys_from_jql(jql)[0]
    labels = ticket['Label'].split(", ")
    formatted_labels = [label.strip().replace(" ", "_") for label in labels]
    fields = {
        "labels": formatted_labels,
        "customfield_10007": "BRM-1",
        "reporter": {
            "name": 'tristan.morris'
        }
    }
    clear_label = tickets.clear_field(key, "labels")
    print(f'Clearing Label status code response: {clear_label}')
    field_response = tickets.set_fields(key, fields)
    print(f"Ticket: {key}, has the field set response of: {field_response}")

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
