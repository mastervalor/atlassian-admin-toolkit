from auth import auth
import json
import requests
from tabulate import tabulate

# url = "https://lucidmotors.atlassian.net/rest/api/3/project"
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
#
# list = []
#
# for i in response:
#     case = {'name': i['name'], 'key': i['key'], 'id': i['id']}
#     list.append(case)
# print(list)
# print(tabulate(list, headers=["Project", "key", "id"]))

url = "https://lucidmotors.atlassian.net/rest/api/3/issue/ATLAS-8712"

payload = json.dumps({
   "fields": {
      "customfield_14052": {
         "key": 'SDLOG'
      },
      "customfield_14116": {
         "value": "Jira"
      }
   }
})
headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)
print(response)
