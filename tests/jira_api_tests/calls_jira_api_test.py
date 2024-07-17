from calls.jira import Jira
from dataformating.json_formating import JSONFormating

jira = Jira()
formating = JSONFormating()


def test_edit_ticket(key, payload):
    edit_ticket = jira.edit_ticket(key, payload)
    print(edit_ticket)
