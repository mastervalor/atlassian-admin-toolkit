import requests
from auth import auth
import json
from logic.jira_logic.group_logic import Groups

group_logic = Groups()


def put(x):
    url = "https://lucidmotors.atlassian.net/rest/api/3/group/user"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    query = {
        'groupname': 'QUAL-Manufacturing-Quality'
    }

    payload = json.dumps({
        "accountId": x
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        params=query,
        auth=auth
    )


groups = ['QUAL-General-Factory-Paint', 'QUAL-General-Factory-BIW', 'QUAL-General-Factory-GA',
          'QUAL-General-Factory-Powertrain', 'QUAL-Incoming-Quality', 'QUAL-PDI', 'QUAL-LCPA']
ids = []
for group in groups:
    response = group_logic.group_members(group)
    for value in json.loads(response)['values']:
        put(value['accountId'])

print(ids)
