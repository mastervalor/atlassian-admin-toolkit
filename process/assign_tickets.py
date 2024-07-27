from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()

jql = ('project = "Corporate Engineering" and summary ~"needs to be rolled over to new standards" and summary !~ '
       '"archived" and assignee is EMPTY')
keys = tickets.get_ticket_keys_from_jql(jql)

assignes = {"swaroop.vimalkumar": 0, "satchidanand.challapalli": 0, "srikanth.racharla": 0}

for key in keys:
    lowest_assignee = min(assignes, key=assignes.get)
    assignee = lowest_assignee
    assignes[lowest_assignee] += 1
    tickets.assign_ticket(key, assignee)
