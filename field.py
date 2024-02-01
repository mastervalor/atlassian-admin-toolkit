import requests
from auth import auth
import json
import re
from tabulate import tabulate

url = "https://jira.robot.car/rest/api/2/auditing/record"

headers = {
    "Accept": "application/json"
}
params = {
    "filter": "customfield_11300"
}
response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth,
    params=params
)

response = json.loads(response.text)
fields = []
#
# for i in response:
#     try:
#         if i['schema']:
#             if ('com.atlassian.jira.toolkit:message' or 'com.atlassian.servicedesk') in i['schema']['custom']:
#                 continue
#             else:
#                 fields.append(
#                     [i['name'], i['schema']['custom'].replace('com.atlassian.jira.plugin.system.customfieldtypes:', '')])
#     except KeyError:
#         continue
#
# print(tabulate(fields, headers=["name", "type"]))

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
# output = json.loads(response.text)
# print(response[0]['schema']['type'])
# for i in response:
# print(i['id'])
