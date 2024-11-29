from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import looker_message_block, looker_inactive_message_block
from file_manip.csv_file_manip import CSVLogic

csv_logic = CSVLogic(open_file='looker owners')

file = csv_logic.read_file()
message_logic = MessageLogic()

for board in file:
    user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
                   'mourad.marzouk@getcruise.com', 'satchidanand.challapalli@getcruise.com',
                   'swaroop.vimalkumar@getcruise.com']

    dashboard_name = board['title']
    dashboard_id = board['dashboard_id']
    if board['Needed?'] == 'N':
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

        blocks = looker_inactive_message_block(creator, updater, dashboard_name, dashboard_id)

    else:
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

        blocks = looker_message_block(creator, updater, dashboard_name, dashboard_id)

    message_logic.send_group_message(user_emails, blocks=blocks)
