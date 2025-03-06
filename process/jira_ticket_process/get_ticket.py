import json
from logic.jira_logic.ticket_logic import Tickets

ticket_logic = Tickets()

response = ticket_logic.get_ticket_by_key("BRM-163")

# owner = response['fields']['status']['name']
# res = response['fields']['resolution']['name']
# assignee = response['fields']['assignee']['name']

# print(owner, res, assignee)
print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
