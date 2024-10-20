import requests
from config import looker_base_url
from calls.looker_api_calls.looker_token_api import LookerToken


class LookerDashboard:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_token = LookerToken()
        self.token = self.looker_token.token

    def get_all_dashboards(self):
        """Retrieve all dashboards and their details."""
        url = f'{self.looker_url}/api/4.0/dashboards'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        return response

    def get_dashboard_by_id(self, dashboard_id):
        """Retrieve details of a specific dashboard by its ID."""
        url = f'{self.looker_url}/api/4.0/dashboards/{dashboard_id}'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        # If the token is expired (401 or 403), refresh the token and retry
        if response.status_code in [401, 403]:
            print(f"Token expired, refreshing token for dashboard {dashboard_id}...")
            self.token = self.looker_token.refresh_token()  # Refresh the token
            headers['Authorization'] = f'token {self.token}'
            response = requests.get(url, headers=headers)

        return response

    def search_dashboards_for_explore(self, explore_name):
        url = f'{self.looker_url}/api/4.0/dashboards/search'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }
        params = {'explore': explore_name}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
