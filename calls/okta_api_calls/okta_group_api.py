from auth import okta_token as token
from config import okta as okta_base_url
import requests
import json


class OktaGroupCalls:

    @classmethod
    def get_group_id(cls, name):
        url = okta_base_url + f'groups?q={name}'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            groups = json.loads(response.text)
            for group in groups:
                if group['profile']['name'] == name:
                    return group['id']
            return "Group not found."
        else:
            return f"Failed to retrieve group ID. Status code: {response.status_code}"

    @classmethod
    def get_group_users(cls, group_id):
        url = okta_base_url + f'groups/{id}/users'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.get(url, headers=headers)

        return json.loads(response.text)
