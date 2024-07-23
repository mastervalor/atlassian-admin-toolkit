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


def text_get_ticket(key):
    ticket = jira.get_ticket(key)
    if ticket.status_code == 200 or ticket.status_code == 204:
        formating.pretty_json(ticket)
    else:
        print(ticket.status_code, ticket.text)


payload = {
    "fields": {
        "customfield_26200": {
            "value": "E3"
        }
    }
}

test_edit_ticket('IMAP-1524', payload)


# test_get_ticket('IMAP-1637')