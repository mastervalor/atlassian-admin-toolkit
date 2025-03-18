from logic.jira_logic.system_logic import JiraSystemsLogic
import json

statuses = JiraSystemsLogic()

print(json.dumps(statuses, sort_keys=True, indent=4, separators=(",", ": ")))
