from call import Okta, call, Confluence, Jira
import json
import requests
from auth import conf_token
from config import confluence
import csv
import os

user = Okta.users_id('rick.barlow@getcruise.com')

# manager = Okta.users_id(user['profile']['manager'] + '@getcruise.com')
# print(manager['profile']['title'])

print(json.dumps(user, sort_keys=True, indent=4, separators=(",", ": ")))