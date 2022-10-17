import requests
from auth import auth
import json


def call_spaces(min, max):
    url = f"https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/?start={min}&limit={max}&expand=description.view"
    # url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/CTD/settings"

    headers = {
        "Accept": "application/json",
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    return response

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))


min = 0
max = 100

while max <= 400:
    response = call_spaces(min, max)
    for i in response['results']:
        if i['status'] != 'current' and i['status'] != 'archived':
            print(i['name'] + ':   ' + i['status'])
    min += 100
    max += 100

