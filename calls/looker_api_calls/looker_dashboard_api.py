import requests
import json
from config import looker_base_url
from looker_token_api import LookerToken


class LookerDashboard:
    def __init__(self):
        self.looker_url = looker_base_url
        self.token = LookerToken.get_access_token()

    def get_all_dashboards(self):
        """Retrieve all dashboards and their details."""
        url = f'{looker_base_url}/api/4.0/dashboards'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        return response
