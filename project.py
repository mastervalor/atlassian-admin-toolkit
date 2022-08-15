import csv
import os
import requests
import json
from auth import auth

updatedfile = 'projects'

url = "https://lucidmotors.atlassian.net/rest/api/3/project?expand=lead,description"

auth = auth

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

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updatedfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project Name', 'Project Key', 'Project Type', 'Project Category', 'Project Description', 'Project Owner'])
    for i in response:
        if i['name'].startswith("[dead]") or i['name'].startswith("{Archived}") or i['name'].startswith("{ARCHIVED}") or "archived" in i:
            continue
        else:
            if "projectCategory" not in i:
                writer.writerow(
                    [i['name'], i['key'], i['projectTypeKey'], 'None', i['description'], i['lead']['displayName']])
            else:
                writer.writerow([i['name'], i['key'], i['projectTypeKey'], i['projectCategory']['name'], i['description'], i['lead']['displayName']])


print('done')

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
