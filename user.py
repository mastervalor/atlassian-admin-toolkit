import requests
import json
from auth import auth

url = "https://lucidmotors.atlassian.net/rest/api/3/user/properties/lucidmotors-userProfile?accountId=557058:beeea11c-94e3-48e5-900a-1b92b17df45e"

headers = {
   "Accept": "application/json"
}


response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
