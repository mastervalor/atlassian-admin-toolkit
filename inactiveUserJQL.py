import requests
from auth import auth
import json
import concurrent.futures
import time


def call(pref, apiAction, payload=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + pref

    if apiAction == 'get':
        headers = {"Accept": "application/json"}
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text

        return json.loads(response)
    elif apiAction == 'search':
        url = "https://lucidmotors.atlassian.net/rest/api/3/search"
        headers = {
            "Accept": "application/json"
        }

        query = {
            'jql': f'project = {pref} and (assignee in inactiveUsers() or reporter in inactiveUsers()) and resolution is EMPTY'
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=auth
        ).text

        return json.loads(response)
    elif apiAction == 'put':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )


def inactive(i):
    id = call(i, 'search')
    status = id['fields']['status']['name']
    if status != ('Done' or 'Canceled' or 'Resolved'):
        assignee = id['fields']['assignee']['active']
        reporter = id['fields']['reporter']['active']
        if not assignee:
            accountId = id['fields']['assignee']['accountId']
            upref = f'user/properties/lucidmotors-userProfile?accountId={accountId}'
            try:
                manager = call(upref, 'get')['value']['manager']
            except KeyError:
                print(f'The Assignee in QUAL-{i} does not have a listed manager')
            payload = json.dumps({
                "fields": {
                    "assignee": {
                        "accountId": manager
                    }
                }
            })
            call(pref, 'put', payload)
            print(f'Assignee was changed on Qual-{i} to {manager}')
        if not reporter:
            accountId = id['fields']['reporter']['accountId']
            upref = f'user/properties/lucidmotors-userProfile?accountId={accountId}'
            try:
                manager = call(upref, 'get')['value']['manager']
            except KeyError:
                print(f'The Reporter in QUAL-{i} does not have a listed manager')
            payload = json.dumps({
                "fields": {
                    "reporter": {
                        "accountId": manager
                    }
                }
            })
            call(pref, 'put', payload)
            print(f'Reporter was changed on Qual-{i} to {manager}')
    else:
        print(f'nothing needed on qual-{i}')
        return


pref = 'project'
response = call(pref, 'get')
projects = []

for i in response:
    if "{Archived}" not in i['name']:
        projects.append(i['key'])

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(inactive, projects)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')
