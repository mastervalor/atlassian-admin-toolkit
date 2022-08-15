import csv
import os
import requests
import json
from auth import auth
from os import path

url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/?start=190&limit=210&expand=description.view"
# url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/CTD/settings"

headers = {
    "Accept": "application/json",
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)

updatedfile = 'spaces_des'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updatedfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Space Name', 'Space Key', 'Desctiption'])
    for i in response['results']:
        writer.writerow([i['name'], i['key'], i['description']['view']['value']])

#print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
