from call import Okta, call, Confluence, Jira
import json
import requests
from auth import conf_token
from config import confluence
import csv
import os

user = Okta.users_id('mo.elshenawy@getcruise.com')

# manager = Okta.users_id(user['profile']['manager'] + '@getcruise.com')
# print(manager['profile']['title'])
print(json.dumps(user, sort_keys=True, indent=4, separators=(",", ": ")))
# manager = Okta.users_id(user['profile']['manager'] + '@getcruise.com')

# status = True
# while status:
#     if manager['status'] == 'DEPROVISIONED':
#         print(manager['profile']['email'] + manager['status'])
#         manager = Okta.users_id(manager['profile']['manager'] + '@getcruise.com')
#     else:
#         status = False
# print(manager['profile']['manager'] + manager['status'])