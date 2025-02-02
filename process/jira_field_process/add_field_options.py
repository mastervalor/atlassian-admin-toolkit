from logic.jira_logic.field_logic import Fields
import json

fields = Fields()

response = fields.field_options(29700, 37300)

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
