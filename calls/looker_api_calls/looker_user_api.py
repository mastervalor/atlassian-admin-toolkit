import requests
import json
from config import looker_base_url
from looker_token_api import LookerToken


class LookerUsers:
    def __init__(self):
        self.looker_url = looker_base_url
        self.token = LookerToken.get_access_token()

    def deactivate_user(self, user_id):
        """Deactivate a user by user ID."""
        url = f'{self.looker_url}/api/4.0/users/{user_id}'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }
        # Update user status to inactive
        data = {
            'is_disabled': True
        }

        response = requests.patch(url, headers=headers, data=json.dumps(data))

        return response

