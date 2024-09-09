import json
from calls.jira import Jira

jira = Jira()

response = jira.get_ticket("BRM-163")

# owner = response['fields']['status']['name']
# res = response['fields']['resolution']['name']
# assignee = response['fields']['assignee']['name']

# print(owner, res, assignee)
print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))