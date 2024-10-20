import requests
from config import looker_base_url
from auth import looker_client_id, looker_client_secret


class LookerToken:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_client_id = looker_client_id
        self.looker_client_secret = looker_client_secret
        self.token = self.get_access_token()

    def get_access_token(self):
        """Authenticate and return an access token."""
        url = f'{looker_base_url}/api/4.0/login'
        data = {
            'client_id': self.looker_client_id,
            'client_secret': self.looker_client_secret
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception(f'Failed to authenticate: {response.content}')

    def refresh_token(self):
        """Refresh and return a new access token."""
        print("Refreshing access token...")
        self.token = self.get_access_token()  # Re-authenticate and get a new token
        print("Token refreshed successfully")
        return self.token
