from call import Jira
import json

jira = Jira()

response = jira.get_customField_context(29700, 37300)

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))