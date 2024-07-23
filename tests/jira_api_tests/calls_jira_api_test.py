from calls.jira import Jira
from dataformating.json_formating import JSONFormating

jira = Jira(is_staging=True)
formating = JSONFormating()


def test_edit_ticket(key, payload):
    edit_ticket = jira.edit_ticket(key, payload)
    if edit_ticket.status_code == 200:
        print(edit_ticket)
    else:
        print(edit_ticket.status_code, edit_ticket.text)

# def test_add_issue_link(inward_issue_key, outward_issue_key, link_type)


def test_get_ticket(key):
    ticket = jira.get_ticket(key)
    if 'errorMessages' in ticket:
        print(f"Returned error message: {ticket['errorMessages']}" )
        print(f"With these errors if any found: {ticket['errors']}")
    else:
        formating.pretty_json(ticket)

        
def test_add_issue_link(inward_issue_key, outward_issue_key, link_type):
    issue_link = jira.add_issue_link(inward_issue_key, outward_issue_key, link_type)
    print(issue_link)

#
# payload = {
#     "fields": {
#         "customfield_26200": {
#             "value": "E3"
#         }
#     }
# }
#
# test_edit_ticket('IMAP-1524', payload)

# test_get_ticket('IMAP-1524')
