from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block, looker_message_block
from logic.os_logic.csv_logic import CSVLogic


csv_logic = CSVLogic(open_file='looker owners')

file = csv_logic.read_file()
message_logic = MessageLogic()

for board in file:
    user_emails = []
    first_names =[]
    if board['creator_status'] == 'Active':
        user_emails.append(board['creator'])
        creator = board['creator'].split("@")[0]
    elif board['creator_manager_status'] == 'ACTIVE':
        user_emails.append(board['creator_manager'])
        creator = board['creator_manager'].split("@")[0]
    else:
        creator = None

    if board['updater_status'] == 'Active':
        user_emails.append(board['updater'])
        updater = board['updater'].split("@")[0]
    elif board['updater_manager_status'] == 'ACTIVE':
        user_emails.append(board['updater_manager'])
        updater = board['updater_manager'].split("@")[0]
    else:
        updater = None

    print(user_emails)
    print(first_names)
