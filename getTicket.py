import json
import requests
from auth import auth

url = "https://lucidmotors.atlassian.net/rest/api/3/issue/ATLAS-8712"

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