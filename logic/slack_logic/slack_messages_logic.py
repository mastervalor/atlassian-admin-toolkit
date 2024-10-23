from calls.slack_api_calls.slack_users_api import SlackUserAPI
from calls.slack_api_calls.slack_messages_api import SlackMessageAPI


class MessageLogic:
    def __init__(self):
        self.user_handler = SlackUserAPI()
        self.message_handler = SlackMessageAPI()

    def send_direct_message(self, user_email, message_text):
        try:
            user_id = self.user_handler.get_user_id(user_email)
            channel_id = self.message_handler.open_direct_message(user_id)
            self.message_handler.send_message(channel_id, message_text)
            print(f"Message sent to {user_email}")
        except Exception as e:
            print(f"Failed to send direct message to {user_email}: {e}")

    def send_group_message(self, user_emails, message_text):
        user_ids = []
        for email in user_emails:
            try:
                user_id = self.user_handler.get_user_id(email)
                user_ids.append(user_id)
            except Exception as e:
                print(f"Failed to get user ID for {email}: {e}")

        if len(user_ids) < 2:
            print("At least two valid users are required for a group message.")
            return

        try:
            channel_id = self.message_handler.open_group_message(user_ids)
            self.message_handler.send_message(channel_id, message_text)
            print(f"Group message sent to {', '.join(user_emails)}")
        except Exception as e:
            print(f"Failed to send group message: {e}")
