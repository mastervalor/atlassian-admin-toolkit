import requests
from config import looker_base_url
from calls.looker_api_calls.looker_token_api import LookerToken


class LookerExplores:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_token = LookerToken()
        self.token = self.looker_token.get_access_token()

    def get_all_explores(self):
        """Retrieve all explores across all models in the system."""
        models_url = f'{self.looker_url}/api/4.0/lookml_models'
        headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/json'
        }

        models_response = requests.get(models_url, headers=headers)

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
    