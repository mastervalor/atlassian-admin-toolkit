import requests
from requests.auth import HTTPBasicAuth
from auth import auth
import json

id = '5c955d42196abe2e884cb02d'

url = "https://lucidmotors.atlassian.net/rest/api/3/user/properties/lucidmotors-userProfile?accountId=" + id

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text

dept = json.loads(response)#['value']['manager']

print(dept)
