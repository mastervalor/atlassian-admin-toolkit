from auth import auth
import json
import requests
from datetime import datetime

url = f"https://jira.robot.car/rest/api/2/search?maxResults=1"

headers = {
        "Accept": "application/json"
    }

query = {
        'jql': 'project = EMSTOP ORDER BY created DESC'
    }

response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
print(response['total'])
date = datetime.strptime(response['issues'][0]['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
print(date.strftime('%B %Y'))
print(response['issues'][0]['key'])


query = {
        'jql': 'project = "IT Apps" ORDER BY created ASC'
    }

response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
date = datetime.strptime(response['issues'][0]['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
print(date.strftime('%B %Y'))
print(response['issues'][0]['key'])