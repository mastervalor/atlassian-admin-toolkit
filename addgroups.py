import requests
from auth import auth
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


def post(group, key, id):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/project/{key}/role/{id}"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "group": [group]
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response


projectRoles = ['10001', '10002', '10301', '10000', '10300', '10425', '10432']
projectType = ['developers', 'admins', 'agents', 'users', 'customers', 'suppliers', 'read-only']
projects = call('project')

for i in projects:
    if i['name'].startswith("[dead]") or i['name'].startswith("{Archived}") or i['name'].startswith("{ARCHIVE}") \
            or ("archived" in i and i['archived'] == 'True'):
        continue
    else:
        for (t, l) in zip(projectType, projectRoles):
            group = f'okta_jira_{i["key"]}_{t}'
            if check_group(group):
                response = post(group, i['key'], l)
                if response.status_code == 200:
                    print(f"This group: {group}, was added to project: {i['key']} with the role of {t}")
                elif response.status_code == 400:
                    print(f"This group: {group}, did not match to project: {i['key']} with the role of {t}")
                else:
                    print(response)
