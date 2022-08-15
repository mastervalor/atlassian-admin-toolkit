import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lucidmotors.atlassian.net/rest/api/3/field/customfield_13512/context/16668/option"

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

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