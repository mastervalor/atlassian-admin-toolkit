from calls.atlassian_admin_api_calls.user_directory_api_calls import UserDirectory


class UserDirectoryLogic:
    def __init__(self):
        self.user_directory = UserDirectory()

    def restore_users(self, users):
        for user in users:
            response = self.user_directory.restore_user(user)
            print(response)



