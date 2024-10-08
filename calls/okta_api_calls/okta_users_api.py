from auth import okta_token
from config import okta
import requests
import json


class OktaUsers:
    def __init__(self):
        self.token = okta_token
        self.okta_base_url = okta
    
    def users_profile(self, email):
        url = self.okta_base_url + 'users'
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            return json.loads(response.text)[0]
        except IndexError:
            return False

