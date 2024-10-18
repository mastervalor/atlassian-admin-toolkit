from calls.looker_api_calls.looker_explores_api import LookerExplores
from dataformating.response_handling import APIResponseHandler
import pandas as pd


class LookerExplorersLogic:
    def __init__(self):
        self.looker_explorers = LookerExplores()

    # def get_all_explores(self):
    #     response = self.looker_explorers.get_all_explores()
    #     handler = APIResponseHandler(response)
    #
    #     if handler.get_status_code() == 200:
    #         print(f"Success: {handler.get_data().get('message', 'No message returned')}")
    #     else:
    #         print(f"Error code:{handler.get_status_code()} Error: {handler.get_error_message()}")
    #     return response.json()

    def get_explores_by_model(self, model_name):
        response = self.looker_explorers.get_all_explores_by_model(model_name)

        if response.get_status_code() == 200:
            print(f"Success: {response.get_data().get('message', 'No message returned')}")
            return response.json()
        else:
            print(f"Error on {model_name} code:{response.get_status_code()} Error: {response.get_error_message()}")

    def get_all_explores(self):
        """Retrieve all explores for all models and return them in a DataFrame with all fields."""
        models = self.looker_explorers.get_all_models()  # Fetch all models, parsed as JSON
        explores_data = []

        # Loop through all models
        for model in models:
            explores = model.get('explores', [])  # Get the explorers for the current model
            for explore in explores:
                # Combine the model and explore data into one dictionary
                combined_data = {**model, **explore}
                explores_data.append(combined_data)
        return explores_data

        # 'model_name': model['name'],
        # 'project_name': model['project_name'],
        # 'explore_name': explore['name'],
        # 'explore_label': explore['label'],
        # 'explore_hidden': explore['hidden'],
        # 'explore_group_label': explore['group_label']
