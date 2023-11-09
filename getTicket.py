import json
from call import Jira

jira = Jira()

response = jira.get_ticket("ITAPP-6403")

owner = response['fields']['status']['name']
res = response['fields']['resolution']['name']

print(owner, res)
# print(json.dumps(owner, sort_keys=True, indent=4, separators=(",", ": ")))