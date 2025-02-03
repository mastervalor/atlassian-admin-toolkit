import requests
from auth import auth
from logic.jira_logic.project_logic import Projects
import json
from group import check_group
import csv
import os


def call(ext):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + ext

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


projectRoles = ['10001', '10002', '10301', '10000', '10300', '10425', '10432']
projectType = ['developers', 'admins', 'agents', 'users', 'customers', 'suppliers', 'read-only']
projects = call('project')
project_logic = Projects()

for i in projects:
    if i['name'].startswith("[dead]") or i['name'].startswith("{Archived}") or i['name'].startswith("{ARCHIVE}") \
            or ("archived" in i and i['archived'] == 'True'):
        continue
    else:
        for (t, l) in zip(projectType, projectRoles):
            group = f'okta_jira_{i["key"]}_{t}'
            if check_group(group):
                response = project_logic.add_group_to_project_by_role(group, l, i['key'])
                if response.status_code == 200:
                    print(f"This group: {group}, was added to project: {i['key']} with the role of {t}")
                elif response.status_code == 400:
                    print(f"This group: {group}, did not match to project: {i['key']} with the role of {t}")
                else:
                    print(response)
