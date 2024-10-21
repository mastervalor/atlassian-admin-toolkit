import requests
from slack_api_handling import APIHandling


class UserAPIClient:
    def __init__(self, token=None):
        self.base_url = 'https://slack.com/api/'
        self.token = token
        self.post_handling = APIHandling()

    def get_user_id(self, user_email):
        url = self.base_url + 'users.lookupByEmail'
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        params = {'email': user_email}
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        if not response_data.get('ok'):
            error = response_data.get('error', 'Unknown error')
            print(f"Slack API error on users.lookupByEmail: {error}")
            return None
        return response_data['user']['id']