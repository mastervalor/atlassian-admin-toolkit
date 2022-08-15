import requests
from auth import auth
import json


def call(pref):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + pref

    headers = {"Accept": "application/json"}
    response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text

    return json.loads(response)

fields = input("Please enter a list of field IDs you are trying to edit seperated by commas? ").split(",")

name = []

for i in fields:
    url = f"https://lucidmotors.atlassian.net/rest/api/3/field/search?id=customfield_{i}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text
    if json.loads(response)['total'] == 0:
        fields.append(str(input(f"Looks like {i} is not correct, Please try again: ")))
    else:
        name.append(json.loads(response)['values'][0]['name'].lower().split("_", 1)[0].replace(" ", "_"))


pref = "issue/ATLAS-3223"
id = call(pref)['fields']['reporter']['accountId']
pref = "user/properties/lucidmotors-userProfile?accountId=" + id
value = call(pref)['value'][name]


13907,13901,13904,13903,13902
'{"fields": {"customfield_13508": {"content": [{"content": [{"text": "check this out kaneka", "type": "text"}], "type": "paragraph"}], "type": "doc", "version": 1}}}'

"assignee": {
            "accountId": "5caccd8a1608c412138787e3",
            "accountType": "atlassian",
            "active": true,
            "avatarUrls": {
                "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5caccd8a1608c412138787e3/6867560a-62a9-4a36-9137-0101127b37f7/16",
                "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5caccd8a1608c412138787e3/6867560a-62a9-4a36-9137-0101127b37f7/24",
                "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5caccd8a1608c412138787e3/6867560a-62a9-4a36-9137-0101127b37f7/32",
                "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5caccd8a1608c412138787e3/6867560a-62a9-4a36-9137-0101127b37f7/48"
            },

    "assignee": {
        "accountId": "5f2c2b96c9c094001cad85aa",
        "accountType": "atlassian",
        "active": true,
        "avatarUrls": {
            "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5f2c2b96c9c094001cad85aa/03d31b3b-73e4-4b67-91c9-a108845e0723/16",
            "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5f2c2b96c9c094001cad85aa/03d31b3b-73e4-4b67-91c9-a108845e0723/24",
            "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5f2c2b96c9c094001cad85aa/03d31b3b-73e4-4b67-91c9-a108845e0723/32",
            "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5f2c2b96c9c094001cad85aa/03d31b3b-73e4-4b67-91c9-a108845e0723/48"
        },
        "displayName": "Mourad Marzouk",
        "emailAddress": "mouradmarzouk@lucidmotors.com",
        "self": "https://lucidmotors.atlassian.net/rest/api/3/user?accountId=5f2c2b96c9c094001cad85aa",
        "timeZone": "America/Los_Angeles"
    },


payload = json.dumps({
  "fields": {
      f"customfield_{ticket}": {
          "content": [
              {
                  "content": [
                      {
                          "text": value,
                          "type": "text"
                      }
                  ],
                  "type": "paragraph"
              }
          ],
          "type": "doc",
          "version": 1
      }

  }
})