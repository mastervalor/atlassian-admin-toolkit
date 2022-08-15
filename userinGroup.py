import requests
from auth import auth
import json
import csv
import os


def call(x, groupName=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + x

    headers = {
        "Accept": "application/json"
    }
    query = ''

    if groupName:
        query = {
            'groupname': groupName
        }
    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)
    return response


newFile = 'project role groups and users'
list = []
listd = []

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='a') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project', 'Role', 'Group', 'users'])

groupName = call('project/AEVSE/role/10001')["actors"]
for y in groupName:
    if y['displayName'].startswith('CC-'):
        list.append(y['displayName'])
    else:
        listd.append(y['displayName'])

# names = call('group/member', groupName['displayName'])['values']
# for x in names:
#     list.append(x['emailAddress'])

print(list)
print(listd)