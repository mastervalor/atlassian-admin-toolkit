from calls.looker_api_calls.looker_explores_api import LookerExplores
from dataformating.response_handling import APIResponseHandler


class LookerExplorersLogic:
    def __init__(self):
        self.looker_explorers = LookerExplores()

    def get_all_explores(self):
        response = self.looker_explorers.get_all_explores()
        handler = APIResponseHandler(response)

        if handler.get_status_code() == 200:
            print(f"Success: {handler.get_data().get('message', 'No message returned')}")
        else:
            print(f"Error code:{handler.get_status_code()} Error: {handler.get_error_message()}")
        return response

    def get_explores_by_model(self, model_name):
        response = self.looker_explorers.get_all_explores_by_model(model_name)

        return response
