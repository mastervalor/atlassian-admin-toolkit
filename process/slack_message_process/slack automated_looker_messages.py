from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='Jira API Integration Tokens Inventory')

file = os_logic.read_file()
message_logic = MessageLogic()

for svc in file:
    user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
                   'mourad.marzouk@getcruise.com', 'satchidanand.challapalli@getcruise.com',
                   'swaroop.vimalkumar@getcruise.com']

