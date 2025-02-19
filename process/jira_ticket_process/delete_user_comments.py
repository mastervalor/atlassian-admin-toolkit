import json
from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
from logic.jira_logic.ticket_logic import Tickets

ticket_logic = Tickets()

ticket = 'ORACLE-3390'
username = 'user-e5e03'

comments = ticket_logic.get_users_comment_ids(username, ticket)

print(comments)
# print(json.dumps(comments, sort_keys=True, indent=4, separators=(",", ": ")))
#3650988, 3650983
