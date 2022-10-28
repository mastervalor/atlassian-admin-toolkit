import requests
from auth import auth
import json
import csv
import os


def call(key, group, role, target):
    url = f"https://lucidmotors-sandbox-693.atlassian.net/wiki/rest/api/space/{key}/permission"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "subject": {
            "type": "group",
            "identifier": group
        },
        "operations": {
            "key": role,
            "target": target
        },
        "_links": {}
    })
    response = json.loads(requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    ).text)
    if response['statusCode'] == 400:
        print(f"Group: {group} in space: {key} with role {role, target}: {response}")
    print(response)
    return response


openFile = 'conflunce role groups and users 2'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for space in csv_reader:
        group = f"okta_confluence_{space['Space key']}_{space['Role']}"
        if space['Role'] == 'editor' or space['Role'] == 'admins':
            call(space['Space key'], group, 'create', 'page')
            call(space['Space key'], group, 'create', 'attachment')
            call(space['Space key'], group, 'create', 'blogpost')
            call(space['Space key'], group, 'create', 'comment')
            call(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with editor rights")
        elif space['Role'] == 'commentor':
            call(space['Space key'], group, 'create', 'comment')
            call(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with commentor rights")
        elif space['Role'] == 'read-only':
            call(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with read-only rights")
