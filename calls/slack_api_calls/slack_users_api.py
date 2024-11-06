from calls.slack_api_calls.slack_api_handling import SlackAPIHandling


class SlackUserAPI:
    def __init__(self):
        self.api_handler = SlackAPIHandling()

    def get_user_id(self, user_email):
        """Fetches the Slack user ID by email, handling rate limits."""
        endpoint = 'users.lookupByEmail'
        params = {'email': user_email}

        try:
            response_data = self.api_handler.get(endpoint, params)
            return response_data['user']['id']
        except Exception as e:
            print(f"Failed to get user ID for {user_email}: {e}")
            return None


