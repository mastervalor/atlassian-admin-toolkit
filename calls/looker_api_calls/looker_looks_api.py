import requests
from config import looker_base_url
from calls.looker_api_calls.looker_token_api import LookerToken


class LooksExplores:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_token = LookerToken()
        self.token = self.looker_token.get_access_token()

    def search_looks_by_explore(self, explore_name):
        headers = {'Authorization': f'token {self.token}'}
        looks_url = f'{self.looker_url}/api/4.0/search_looks'
        params = {'explore': explore_name}
        response = requests.get(looks_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to search looks by explore: {response.text}')
