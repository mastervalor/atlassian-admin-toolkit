from call import Jira
import json

jira = Jira()

response = jira.get_workflows()
print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))