import csv
import os
import requests
import json
from auth import auth
from os import path



fileName = "old_new"
updatedfile = 'new'
if not path.exists('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName)):
    print("Sorry that file name doesn't exist, try again")
    quit()

number = {}
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        number[i['newstring']] = i['oldstring']
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updatedfile), mode='w') as new_csv:
        writer = csv.writer(new_csv)
        writer.writerow(['oldstring', 'issueid', 'type', 'parentkey'])
        for t in csv_reader:
            url = f"https://lucidmotors.atlassian.net/rest/api/3/issue/GAR-{t['newstring']}"
            headers = {
                "Accept": "application/json"
            }

            response = requests.request(
                "GET",
                url,
                headers=headers,
                auth=auth
            )

            issue_id = json.loads(response.text)['id']
            type = json.loads(response.text)['fields']['issuetype']['name']
            if type == 'Sub-task':
                parent = json.loads(response.text)['fields']['parent']['key']
                if 'GAR-' in parent:
                    parent = parent.replace('GAR-', '')
                    parent = number[parent]
                elif 'YTSJW-' in parent:
                    parent = parent.replace('YTSJW-', '')
                    parent = number[parent]
                writer.writerow([t['oldstring'], issue_id, type, parent])
            else:
                writer.writerow([t['oldstring'], issue_id, type, 'x'])
