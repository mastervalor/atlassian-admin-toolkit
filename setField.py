import requests
import json
from auth import auth

url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/3/issue/QUAL-5412"

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

value = 'tesing a new script 3'
ticket = '13903'
manager = '5c66057d9854722ed6778985'
payload = json.dumps({
        "fields": {
            "assignee": {
                "accountId": manager
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

print(response)