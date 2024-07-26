from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()

jql = ('project = "Corporate Engineering" and summary ~"needs to be rolled over to new standards" and summary !~ '
       '"archived" and assignee is EMPTY')
keys = tickets.get_ticket_keys_from_jql(jql)

assignes = {"swaroop": 0, "srik": 0, "anand": 0}

for key in keys:
