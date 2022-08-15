import requests
import json
from auth import auth

url = "https://lucidmotors.atlassian.net/secure/MoveIssue.jspa"
payload = 'pid=14152&issuetype=&id=10401&Next=Next&atl_token=BYQY-HL1J-05CD-6X8L_6aad85feb1984dd1fcaf7b04660fe2ade9af8d02_lin'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

url = "https://davidknight.atlassian.net/secure/MoveIssueConfirm.jspa"
payload='confirm=true&id=407788&Confirm=Confirm&atl_token=BYQY-HL1J-05CD-6X8L_6aad85feb1984dd1fcaf7b04660fe2ade9af8d02_lin'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)