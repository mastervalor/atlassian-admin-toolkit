from auth import auth
import json
import requests
from tabulate import tabulate

url = "https://lucidmotors.atlassian.net/rest/api/3/project?expand=lead"

headers = {
    "Accept": "application/json"
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)

list = []

x = 1
for i in response:
    list.append([x, i['name'], i['key'], i['lead']['displayName']])
    x += 1

print(tabulate(list, headers=["total", "Project", "key", "Owner"]))

# print(list)

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
