from auth import conf_token
import requests
import json

url = 'https://wiki.robot.car/rest/api/content/390260181?expand=ancestors'

headers = {
    "Authorization": conf_token,
    "Content-Type": "application/json"}

response = requests.request(
   "GET",
   url,
   headers=headers
)


print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))







