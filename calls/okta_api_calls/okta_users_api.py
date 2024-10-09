from auth import okta_token as token
from config import okta as okta_base_url
import requests
import json


class OktaUsersCalls:

    @classmethod
    def users_profile(cls, email):
        url = okta_base_url + 'users'
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            return json.loads(response.text)[0]
        except IndexError:
            return False
        except KeyError:
            return False

