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

for i in response:
    list.append([i['name'], i['key'], i['lead']['displayName']])

print(tabulate(list, headers=["Project", "key", "Owner"]))

#print(list)

#print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
