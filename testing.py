# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lucidmotors.atlassian.net/rest/api/3/workflow/search?workflowName=AAAAAAA"

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

headers = {
   "Accept": "application/json"
}

# workflow = json.loads(requests.get(url,auth=auth, headers=headers).text)

workflow = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
).text

workflow = json.loads(workflow)

id = workflow['values'][0]['id']['entityId']

print(id)
