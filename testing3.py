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
