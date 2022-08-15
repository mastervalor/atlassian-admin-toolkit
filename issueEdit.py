import requests
from auth import auth
import json

url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/3/issue/TES-2"


headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps({
   "fields": {
      "parent":{},
      "issuetype": {
         "id": "5",
      }
   }
})

response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)


print(response.status_code)