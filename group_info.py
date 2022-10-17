import requests
import json
from auth import auth


def call_group(min, max, group):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/group/member?start={min}&limit={max}"

    headers = {
        "Accept": "application/json"
    }
    query = {
        'groupname': group
    }
    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)

    return response


def get_group_users(group):
    min = 0
    max = 50
    total = 50
    users = []

    while max <= total:
        response = call_group(min, max, group)
        if group != 'administrators':
            for i in response['values']:
                try:
                    users.append(i['emailAddress'])
                except KeyError:
                    print(f'User Id {i["accountId"]} was not caught in the group grab')
            min += 50
            max += 50
            total = response['total']
            print(f'group {group} has is the new min {min} and max {max} and the total is {total}')
    print(users)
    return users


get_group_users('CARE-Internal-Authors')
