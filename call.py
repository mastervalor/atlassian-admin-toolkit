import requests
from requests.auth import HTTPBasicAuth
from auth import auth
import json

def call(pref, apiAction, payload=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + pref

    if apiAction == 'get':
        headers = {"Accept": "application/json"}
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text

        return json.loads(response)
    elif apiAction == 'put':
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )