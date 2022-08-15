import requests
import json
from auth import auth

url = "https://lucidmotors.atlassian.net/rest/api/3/user/properties/lucidmotors-userProfile?accountId=557058:b210a302-ce69-4752-94f1-fd2529a033a3"

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
