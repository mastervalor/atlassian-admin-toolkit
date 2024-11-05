from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import looker_message_block, looker_inactive_message_block
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners')

file = os_logic.read_file()
message_logic = MessageLogic()

for board in file:
    user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
                   'mourad.marzouk@getcruise.com', 'satchidanand.challapalli@getcruise.com',
                   'swaroop.vimalkumar@getcruise.com']

    dashboard_name = board['title']
    dashboard_id = board['dashboard_id']
    if board['Needed?'] == 'N':
        if board['creator_status'] == 'Active':
            creator = board['creator']
        elif board['creator_manager_status'] == 'ACTIVE':
            creator = board['creator_manager']
        else:
            creator = None

        if board['updater_status'] == 'Active':
            updater = board['updater']
        elif board['updater_manager_status'] == 'ACTIVE':
            updater = board['updater_manager']
        else:
            updater = None

        blocks = looker_inactive_message_block(creator, updater, dashboard_name, dashboard_id)

    else:
        if board['creator_status'] == 'Active':
            creator = board['creator']
        elif board['creator_manager_status'] == 'ACTIVE':
            creator = board['creator_manager']
        else:
            creator = None

        if board['updater_status'] == 'Active':
            updater = board['updater']
        elif board['updater_manager_status'] == 'ACTIVE':
            updater = board['updater_manager']
        else:
            updater = None

        blocks = looker_message_block(creator, updater, dashboard_name, dashboard_id)

    message_logic.send_group_message(user_emails, blocks=blocks)
