import requests
from requests.auth import HTTPBasicAuth
from auth import auth
import json

url = "https://lucidmotors.atlassian.net/rest/api/3/issue/QFT-15"


response = requests.request(
   "DELETE",
   url,
   auth=auth
)

print(response.text)