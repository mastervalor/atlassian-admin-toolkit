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


def check_group(group):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/group"

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

    if 'errorMessages' in response:
        return False
    else:
        return True


# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
