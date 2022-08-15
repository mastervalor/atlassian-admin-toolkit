import csv
import os
import requests
import json
from auth import auth
from os import path


url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/?&limit=300"

headers = {
    "Accept": "application/json",
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)

names = []
keys = []
owners = []
powners = []
confirmed = []

fileName = 'space_owners2'
updatedfile = 'spaces'
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        names.append(i['Name'])
        keys.append(i['Key'])
        owners.append(i['Space Owner'])
        powners.append(i['Possible owners'])
        confirmed.append(i['Owner Dept Confirmed'])
        # list[i['name']] = i['key']
        # list[i['name']] = i['_expandable']['description']
    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updatedfile), mode='w') as new_csv:
        writer = csv.writer(new_csv)
        writer.writerow(['Space Name', 'Space Key', 'Space Owner', 'Possible Owners', 'Confirmed'])
        t = 0
        y= keys[t]
        for i in response['results']:
            a = i['key']
            if i['name'] == names[t]:
                writer.writerow([names[t], keys[t], owners[t], powners[t], confirmed[t]])
                print('yes')
                t += 1
            else:
                writer.writerow([i['name'], i['key'], '', '', ''])
                print('no')

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
