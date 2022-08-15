import requests
from auth import auth
import json
import csv
import os


def call(ext, groupName=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + ext

    headers = {
        "Accept": "application/json"
    }
    query = ''

    if groupName:
        query = {
            'groupname': groupName
        }
    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    ).text)
    return response


projectRoles = ['10001', '10301', '10000', '10300', '10425']
projectType = ['Developers', 'agents', 'users', 'customers', 'suppliers']
newFile = 'project role groups and users'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project', 'Role', 'Cost Center/emails'])
    projects = call('project')
    for i in projects:
        if i['name'].startswith("[dead]") or i['name'].startswith("{Archived}") or i['name'].startswith("{ARCHIVE}") \
                or ("archived" in i and i['archived'] == 'True'):
            continue
        else:
            for (a, r) in zip(projectRoles, projectType):
                groupName = call(f'project/{i["key"]}/role/{a}')
                if 'actors' in groupName:
                    emails = []
                    costCenters = []
                    for x in groupName['actors']:
                        if x['displayName'].startswith('CC-') or x['displayName'].startswith('DEPT-') or \
                                x['displayName'].startswith('grp-') or x['displayName'].startswith('okta_'):
                            costCenters.append(x['displayName'])
                        else:
                            names = call('group/member', x['displayName'])
                            if 'values' in names:
                                for y in names['values']:
                                    emails.append(y['emailAddress'])
                    if costCenters:
                        writer.writerow([i['name'], r, costCenters])
                    if emails:
                        writer.writerow([i['name'], r, emails])
