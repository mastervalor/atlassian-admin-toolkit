from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners')

file = os_logic.read_file()
message_logic = MessageLogic()

for board in file:
    # user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
    #                'mourad.marzouk@getcruise.com', 'satchidanand.challapalli@getcruise.com',
    #                'swaroop.vimalkumar@getcruise.com']
    if board['Needed?'] == 'N':
        if board['creator'] == 'Active':
            creator = board['creator']
        elif board['creator_manager_status'] == 'ACTIVE':
            creator = board['creator_manager']

