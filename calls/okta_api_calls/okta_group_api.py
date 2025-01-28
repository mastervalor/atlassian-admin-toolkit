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

        return json.loads(response.text)[0]['id']

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
