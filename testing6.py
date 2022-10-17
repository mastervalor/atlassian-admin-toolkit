import csv
import os
import requests
import json
from auth import auth
from group import get_group_users

# updatedfile = 'projects'
#
# url = "https://lucidmotors.atlassian.net/rest/api/3/project?expand=lead"
#
# auth = auth
#
# headers = {
#     "Accept": "application/json"
# }
#
# response = json.loads(requests.request(
#     "GET",
#     url,
#     headers=headers,
#     auth=auth
# ).text)

EDITORS = []
COMMENTORS = []
READ_ONLY = []


def call(key):
    url = f"https://lucidmotors.atlassian.net/wiki/rest/api/space/{key}?expand=permissions"

    headers = {
        "Accept": "application/json"
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    return response


def add_perm(group, role):
    if group == "administrators":
        return False
    if group.startswith('cc-') or group.startswith('dept-') or \
            group.startswith('grp-') or group.startswith('okta_') or group.startswith('division') or group == 'engineering':
        if 'page create' in role or 'attachment create' in role or 'blogpost create' in role:
            EDITORS.append(group)
        elif 'comment create' in role:
            COMMENTORS.append(group)
        elif 'space read' in role:
            READ_ONLY.append(group)
    else:
        emails = get_group_users(group)
        for email in emails:
            if 'page create' in role or 'attachment create' in role or 'blogpost create' in role:
                EDITORS.append(email)
            elif 'comment create' in role:
                COMMENTORS.append(email)
            elif 'space read' in role:
                READ_ONLY.append(email)


openFile = 'spaces_des2'
user = ''
group = ''
role = []

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for space in csv_reader:
        response = call(space['Space Key'])
        EDITORS = []
        COMMENTORS = []
        READ_ONLY = []
        group = ''
        role = []
        for i in response['permissions']:
            try:
                if group == '':
                    group = i['subjects']['group']['results'][0]['name']
                if i['subjects']['group']['results'][0]['name'] == 'confluence-users':
                    continue
                if i['subjects']['group']['results'][0]['name'] != 'administrators':
                    if group != i['subjects']['group']['results'][0]['name']:
                        add_perm(group, role)
                        group = i['subjects']['group']['results'][0]['name']
                        role.clear()
                        role.append(i['operation']['targetType'] + ' ' + i['operation']['operation'])
                    elif group == i['subjects']['group']['results'][0]['name']:
                        role.append(i['operation']['targetType'] + ' ' + i['operation']['operation'])
            except KeyError:
                try:
                    if 'Unlicensed' in i['subjects']['user']['results'][0]['displayName']:
                        print(
                            f"found and inactive users {i['subjects']['user']['results'][0]['displayName']} in the {space['Space Key']}")
                    else:
                        if user != i['subjects']['group']['results'][0]['displayName'] or user == '':
                            user = i['subjects']['group']['results'][0]['displayName']
                            print(space['Space Key'] + ":  displayName   " + user)
                except KeyError:
                    continue
        add_perm(group, role)
        if EDITORS:
            print(f"the editos for {space['Space Key']} are:")
            print(EDITORS)
        if COMMENTORS:
            print(f"the commentors for {space['Space Key']} are: ")
            print(COMMENTORS)
        if READ_ONLY:
            print(f"the read only for {space['Space Key']} are")
            print(READ_ONLY)
