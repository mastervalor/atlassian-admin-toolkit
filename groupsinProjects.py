import requests
from auth import auth
import json
import csv
import os
from logic.confluence_logic.groups_logic import ConfGroupLogic
from logic.confluence_logic.space_logic import Spaces


def call(ext, id=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + ext

    headers = {
        "Accept": "application/json"
    }
    query = ''

    if id:
        query = {
            'accountId': id
        }
    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)
    return response


project_roles = ['10001', '10002', '10301', '10000', '10300', '10425', '10432']
project_type = ['developers', 'admins', 'agents', 'users', 'customers', 'suppliers', 'read-only']
new_file = 'project role groups and users 3'
conf_groups = ConfGroupLogic()
conf_space_logic = Spaces()

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), new_file), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['jira', 'Project key', 'Role', 'Cost Center'])
    projects = call('project')
    for i in projects:
        if i['name'].startswith("[dead]") or i['name'].startswith("{Archived}") or i['name'].startswith("{ARCHIVE}") \
                or ("archived" in i and i['archived'] == 'True'):
            continue
        else:
            for (a, r) in zip(project_roles, project_type):
                groupName = call(f'project/{i["key"]}/role/{a}')
                if 'actors' in groupName:
                    emails = []
                    costCenters = []
                    users = []
                    for x in groupName['actors']:
                        if x['displayName'] != 'administrators':
                            if x['displayName'].startswith('CC-') or x['displayName'].startswith('DEPT-') or \
                                    x['displayName'].startswith('grp-') or x['displayName'].startswith('okta_'):
                                costCenters.append(x['displayName'])
                            else:
                                names = conf_groups.get_group_users_email(x['displayName'])
                                if 'errorMessages' in names:
                                    user = call('/user', x['actorUser']['accountId'])
                                    try:
                                        users.append(user['emailAddress'])
                                    except KeyError:
                                        print(x['actorUser']['accountId'], x['displayName'], i['key'], a)
                                if 'values' in names:
                                    for y in names['values']:
                                        try:
                                            emails.append(y['emailAddress'])
                                        except KeyError:
                                            print(y['accountId'], y['displayName'], i['key'], a)
                    if costCenters or emails or users:
                        writer.writerow(['jira', i['key'], r, costCenters + emails + users])
