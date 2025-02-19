from auth import conf_token
import requests
import json

url = 'https://wiki.robot.car/rest/api/content/500924168'

headers = {
    "Authorization": conf_token,
    "Accept": "application/json",
    "Content-Type": "application/json"}

payload = json.dumps({
  "version": {
    "number": 2,
  },
  "title": "test move page",
  "type": "page",
  "status": "current",
  "ancestors": [
    {
      "id": 433434679
    }
  ],
})

response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers
)


print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


