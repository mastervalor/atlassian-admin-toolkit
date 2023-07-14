from call import Okta, call, Confluence, Jira
import json
import requests
from auth import conf_token
from config import confluence
import csv
import os

user = Okta.users_id('ilya.subkhankulov@getcruise.com')
manager = Okta.users_id(user['profile']['manager'] + '@getcruise.com')
status = True
while status:
    if manager['status'] == 'DEPROVISIONED':
        print(manager['profile']['email'] + ' ' + manager['status'])
        manager = Okta.users_id(manager['profile']['manager'] + '@getcruise.com')
    else:
        status = False
print(manager['profile']['email'] + ' ' + manager['profile']['title'])
print(manager['profile']['firstName'] + ' ' + manager['profile']['lastName'])
if "Vice President" in manager['profile']['title'] or "VP," in manager['profile']['title'] or "chief" in manager['profile']['title']:
    reports = manager['profile']['directReports']
    print(reports)
    name_list = reports.split("; ")
    for report in name_list:
        email = f"{report.lower().replace(' ', '.')}@getcruise.com"
        looking = Okta.users_id(email)
        if 'Executive Assistant' in looking['profile']['title'] or 'Executive Business' in looking['profile']['title']:
            assistant = report
            print(manager['profile']['firstName'] + ' ' + manager['profile']['lastName'])
            print(report + ' ' + looking['profile']['title'])
            break



# print(manager['profile']['title'])
# print(json.dumps(user, sort_keys=True, indent=4, separators=(",", ": ")))


# print(manager['profile']['manager'] + manager['status'])