import json
from logic.jira_logic.project_logic import Projects


project_logic = Projects()

move = project_logic.move_components_between_projects('SEC', "THREAT")

print(json.dumps(move, sort_keys=True, indent=4, separators=(",", ": ")))