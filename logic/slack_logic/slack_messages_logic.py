from calls.slack_api_calls.slack_users_api import SlackUserAPI
from calls.slack_api_calls.slack_messages_api import SlackMessageAPI


class MessageLogic:
    def __init__(self):
        self.user_handler = SlackUserAPI()
        self.message_handler = SlackMessageAPI()

    def send_direct_message(self, user_email, message_text=None, blocks=None):
        """Sends a direct message to an individual user."""
        try:
            user_id = self.user_handler.get_user_id(user_email)
            if user_id:
                channel_id = self.message_handler.open_direct_message(user_id)
                self.message_handler.send_message(channel_id, text=message_text, blocks=blocks)
                print(f"Message sent to {user_email}")
            else:
                print(f"User ID not found for {user_email}")
        except Exception as e:
            print(f"Failed to send direct message to {user_email}: {e}")

    def send_group_message(self, user_emails, message_text=None, blocks=None):
        """Creates a group chat if needed and sends a message to multiple users."""
        user_ids = []
        for email in user_emails:
            user_id = self.user_handler.get_user_id(email)
            if user_id:
                user_ids.append(user_id)
            else:
                print(f"Skipping user {email} due to missing ID or rate limiting.")

        if len(user_ids) < 2:
            print("At least two valid users are required for a group message.")
            return

        try:
            # Check if a group already exists with these users
            channel_id = self.message_handler.get_existing_group_channel(user_ids)
            if not channel_id:
                channel_id = self.message_handler.open_group_message(user_ids)
                print(f"New group chat created for users: {', '.join(user_emails)}")
            else:
                print(f"Using existing group chat for users: {', '.join(user_emails)}")

            # Send the message to the group channel
            self.message_handler.send_message(channel_id, text=message_text, blocks=blocks)
            print(f"Group message sent to {', '.join(user_emails)}")
        except Exception as e:
            print(f"Failed to send group message: {e}")
