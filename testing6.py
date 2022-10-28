import csv
import os
import requests
import json
from auth import auth


def call(key, group, role):
    url = f"https://lucidmotors.atlassian.net/wiki/rest/api/space/{key}/permission"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if role == 'editor' or role == 'admins':
        payload = [
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'create',
                    "target": 'page'
                }
            }),
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'create',
                    "target": 'attachment'
                }
            }),
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'create',
                    "target": 'blogpost'
                }
            }),
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'create',
                    "target": 'comment'
                }
            }),
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'read',
                    "target": 'space'
                }
            })
        ]
    elif role == 'commentor':
        payload = [
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'create',
                    "target": 'comment'
                }
            }),
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'read',
                    "target": 'space'
                }
            })
        ]
    elif role == 'read-only':
        payload = [
            json.dumps({
                "subject": {
                    "identifier": group,
                    "type": "group"
                },
                "operation": {
                    "key": 'read',
                    "target": 'space'
                }
            })
        ]

    for i in payload:
        response = json.loads(requests.request(
            "POST",
            url,
            data=i,
            headers=headers,
            auth=auth
        ).text)
    return response


openFile = 'conflunce role groups and users 2'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for space in csv_reader:
        group = f"okta_confluence_{space['Space key']}_{space['Role']}"
        response = call(space['Space key'], group, space['Role'])
        if 'statusCode' in response:
            print(f"Status code {response['statusCode']}: {response['message']}")
        else:
            print(f"Group {response['subject']['identifier']} was added to {space['Space key']} with the permissions of {response['operation']['target']} {response['operation']['key']}")
