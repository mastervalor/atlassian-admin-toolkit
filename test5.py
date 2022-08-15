import requests
import json
from auth import auth

url = "https://api.atlassian.com/ex/confluence/8c456a13-53e0-4a30-8cbd-3edd74f85b8c/wiki/rest/api/space/homologation?expand=permissions"

headers = {
    "Accept": "application/json",
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)
#
# for a in responseg["permissions"]:
#     keys.append(a['subjects']['group']['results'][0]['name'])
#
#     print(keys)
for a in response["permissions"]:
    try:
        print(a['subjects']['group']['results'][0]['name'])
    except KeyError:
        continue
 # print(a['subjects']['group']['results'][0]['name'], i['name'])
# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
