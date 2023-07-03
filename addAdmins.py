from call import call
import csv
import os
import requests
import json
from auth import auth, staging_auth

# openFile = "Projects No Admin Role"
# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for key in csv_reader:
url = f"https://jira.robot.car/rest/api/2/project/plm/role/10002"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = json.dumps({
    "group": [
        "administrators"
    ]
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))