import csv
import os
import requests
import json
from auth import auth
from os import path


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

mainFile = 'spaces_des'
updatedfile = 'spaces_des2'
min = 0
max = 100

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updatedfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Space Name', 'Space Key', 'Owners'])
    while max <= 400:
        response = call_spaces(min, max)
        for i in response['results']:
            if i['status'] == 'current':
                with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for r in csv_reader:
                        if r['Space Name'] == i['name']:
                            writer.writerow([i['name'], i['key'], r['Owners']])
        min += 100
        max += 100

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
