import requests
from auth import auth
import json
from logic.jira_logic.group_logic import Groups

group_logic = Groups()

groups = ['QUAL-General-Factory-Paint', 'QUAL-General-Factory-BIW', 'QUAL-General-Factory-GA',
          'QUAL-General-Factory-Powertrain', 'QUAL-Incoming-Quality', 'QUAL-PDI', 'QUAL-LCPA']
ids = []
for group in groups:
    response = group_logic.group_members(group)
    for value in json.loads(response)['values']:
        put(value['accountId'])

print(ids)
