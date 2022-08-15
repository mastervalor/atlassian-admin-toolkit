import requests
import json
from auth import auth


def call(pref):
    url = "https://lucidmotors.atlassian.net/rest/api/3/search"
    headers = {
        "Accept": "application/json"
    }
    query = {
        'jql': f'project = {pref} and (assignee in inactiveUsers() or reporter in inactiveUsers()) and resolution is EMPTY',
        'maxResults': 100
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

    return response


urlp = "https://lucidmotors.atlassian.net/rest/api/3/project"

auth = auth

headers = {
    "Accept": "application/json"
}

response = json.loads(requests.request(
    "GET",
    urlp,
    headers=headers,
    auth=auth
).text)

list = []

for i in response:
    if "{Archived}" not in i['name']:
        list.append(i['key'])


for project in list:
    keys = []
    urls = "https://lucidmotors.atlassian.net/rest/api/3/search"
    query = {
        'jql': f'project = {project} and (assignee in inactiveUsers() or reporter in inactiveUsers()) and resolution is EMPTY',
        'maxResults': 100
    }

    response = json.loads(requests.request("GET", urls, headers=headers, params=query, auth=auth).text)

    if response['total'] == 0:
        print(response)
    else:
        for i in response['issues']:
            keys.append(i['key'])
        print(keys)
