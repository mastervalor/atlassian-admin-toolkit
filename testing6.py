import csv
import os
import requests
import json
from auth import auth

updatedfile = 'projects'

url = "https://lucidmotors.atlassian.net/rest/api/3/project?expand=lead"

auth = auth

headers = {
    "Accept": "application/json"
}

response = json.loads(requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
).text)

