import requests
import json
from config import looker_base_url
from calls.looker_api_calls.looker_token_api import LookerToken


class LookerExplores:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_token = LookerToken()
        self.token = self.looker_token.get_access_token()

    def get_all_models(self):
        """Fetch all LookML models."""
        url = f'{self.looker_url}/api/4.0/lookml_models'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }
        models_response = json.loads(requests.get(url, headers=headers).text)

        return models_response

    def get_all_explores_by_model(self, model_name):
        """Retrieve all explores for a specific model."""
        url = f'{self.looker_url}/api/4.0/lookml_models/{model_name}/explores'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        return response

    def get_query_history(self, model_name, explore_name, fields=None, add_drills_metadata=True):
        headers = {'Authorization': f'token {self.token}'}
        explore_url = f'{self.looker_url}/api/4.0/lookml_models/{model_name}/explores/{explore_name}'
        params = {
            'fields': fields,
            'add_drills_metadata': str(add_drills_metadata).lower()
        }
        response = requests.get(explore_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to get query history: {response.text}')
