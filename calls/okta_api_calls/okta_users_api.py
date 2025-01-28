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

    @classmethod
    def get_user_groups(cls, user_id):
        """
        Handles the API call to fetch groups for a given user.
        """
        groups_url = okta_base_url + f'users/{user_id}/groups'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token
        }
        response = requests.get(groups_url, headers=headers, timeout=9000)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error fetching groups: {response.status_code} - {response.text}')

    @classmethod
    def get_user_manager(cls, email):
        url = okta_base_url + 'users'
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            manager = json.loads(response.text)[0]['profile']['manager']
            if not manager:
                return 'empty'
            else:
                return manager
        except KeyError:
            return 'No Manager'
        except IndexError:
            return 'Nothing for this one'
