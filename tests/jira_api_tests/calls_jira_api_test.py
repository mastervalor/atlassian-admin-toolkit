from calls.jira import Jira
from dataformating.json_formating import JSONFormating

jira = Jira()
formating = JSONFormating()


def test_edit_ticket(key, payload):
    edit_ticket = jira.edit_ticket(key, payload)
    print(edit_ticket)


def test_get_ticket(key):
    ticket = jira.get_ticket(key)
    formating.pretty_json(ticket)



# payload = {
#     "fields":
#         "customfield_26200": {"value": "E3"}
#     }