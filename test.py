import requests
from auth import auth
import json

url = "https://lucidmotors.atlassian.net/rest/api/3/search"

headers = {
   "Accept": "application/json"
}

jql = 'project = W20 and (assignee in inactiveUsers() or reporter in inactiveUsers()) and resolution is EMPTY'

query = {
   'jql': jql,
   'startAt' : 0,
   'maxResults': 100
}

list = []

response = json.loads(requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
).text)

for i in response['issues']:
   list.append(i['key'])

length = len(list)

if response['total'] != length:
   loopneeded = True
   while loopneeded:
      query = {
         'jql': jql,
         'startAt': length,
         'maxResults': 100
      }
      response = json.loads(requests.request(
         "GET",
         url,
         headers=headers,
         params=query,
         auth=auth
      ).text)
      for i in response['issues']:
         list.append(i['key'])
      length = len(list)
      if response['total'] == length:
         loopneeded = False


print(length)
print(list)