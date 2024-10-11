from calls.looker_api_calls.looker_user_api import LookerUsers


class LookerUserLogic:
    def __init__(self):
        self.looker_user = LookerUsers

    def deactivate_users(self, user_ids):
        for user_id in user_ids:
            response = self.looker_user.deactivate_user(user_id)

            if response.status_code == 200:
                print(f'User {user_id} deactivated successfully.')
            else:
                print(f'Failed to deactivate user {user_id}: {response.content}')
                