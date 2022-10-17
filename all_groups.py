import requests
from auth import auth
import json


def get_groups(min, max):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/group/bulk?mstart={min}&limit={max}"

    headers = {
        "Accept": "application/json"
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    # print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
    return response


def get_all_groups():
    min = 0
    max = 100
    total = 100
    groups = []
    while max <= total:
        response = get_groups(min, max)
        for i in response['values']:
            groups.append(i['name'])
        min += 100
        max += 100
        total = response['total']

    return groups
    # print(groups)
