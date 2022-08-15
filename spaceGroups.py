import requests
import json
from auth import auth
import csv
import os

url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/?&limit=300"

headers = {
    "Accept": "application/json",
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)

old = ''
new = ''
newFile = 'confluence groups '

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Group', 'Space'])
    for i in response['results']:
            urlg = f"https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/{i['key']}?expand=permissions"

            headers = {
                "Accept": "application/json",
            }

            response = json.loads(requests.request(
                "GET",
                urlg,
                headers=headers,
                auth=auth
            ).text)

            for a in response["permissions"]:
                try:
                    old = a['subjects']['group']['results'][0]['name']
                    if old != new:
                        new = a['subjects']['group']['results'][0]['name']
                        if new in ['grp-atl-confluence', 'atieva-users', 'confluence-users', 'grp-atlassian', 'jira-users']:
                            writer.writerow([new, i['name']])
                except KeyError:
                    continue
