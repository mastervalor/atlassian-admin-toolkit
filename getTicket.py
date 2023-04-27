import json
import requests
from auth import auth

url = "https://jira.robot.car/rest/api/2/issue/NO-691"

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