import requests
from auth import auth
import json


def call(x):
    url = "https://lucidmotors.atlassian.net/rest/api/3/group/member"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'groupname': x
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text

    return response


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
for x in groups:
    response = call(x)
    for i in json.loads(response)['values']:
        put(i['accountId'])

print(ids)
