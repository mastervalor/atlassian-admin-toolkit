import requests
from requests.auth import HTTPBasicAuth
import json
from auth import conf_cloud_dev_token

url = "https://getcruise-sandbox-515.atlassian.net/rest/api/3/field/customfield_11101/context/11658/option"

auth = conf_cloud_dev_token

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