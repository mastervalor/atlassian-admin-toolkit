import requests
from auth import auth
import json

url = "https://lucidmotors.atlassian.net/rest/api/3/issue/422955"



headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.loads(response.text)['fields']['issuetype']['name'])
#print(json.loads(response.text)['fields']['parent']['key'])


print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))