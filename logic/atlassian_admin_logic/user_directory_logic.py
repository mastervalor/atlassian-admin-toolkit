from calls.atlassian_admin_api_calls.user_directory_api_calls import UserDirectory
from dataformating.response_handling import APIResponseHandler


class UserDirectoryLogic:
    def __init__(self):
        self.user_directory = UserDirectory()

    def restore_users(self, users):
        for user in users:
            response = self.user_directory.restore_user(user)
            handler = APIResponseHandler(response)

            if handler.get_status_code() == 200:
                print(f"Success: {handler.get_data().get('message', 'No message returned')}")
            else:
                print(f"Error code:{handler.get_status_code()} Error: {handler.get_error_message()}")

