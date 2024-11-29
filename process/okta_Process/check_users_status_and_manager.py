from logic.okta_logic.okta_user_logic import OktaUsers
from file_manip.csv_file_manip import CSVLogic

csv_logic = CSVLogic(open_file='looker Final List', write_file='looker users')

read_file = csv_logic.read_file()
active_users = []

for user in read_file:
    board = {'title': user['title']}
    if user['created_by']:
        creator = user['created_by'].replace(' ', '.').lower()
        creator_status = OktaUsers.get_user_status(creator)
        manager, manager_title, manager_status = OktaUsers.get_manager_info(creator)
        board['creator'] = user['created_by']
        board['creator_status'] = creator_status
        board['creator_manager'] = manager
        board['creator_manager_title'] = manager_title
        board['creator_manager_status'] = manager_status
        print("Creator and status: ",  creator, creator_status)
    else:
        board['creator'] = ' '
        board['creator_status'] = ' '
        board['creator_manager'] = ' '
        board['creator_manager_title'] = ' '
        board['creator_manager_status'] = ' '

    if user['last_updated_by']:
        updater = user['last_updated_by'].replace(' ', '.').lower()
        updater_status = OktaUsers.get_user_status(updater)
        manager, manager_title, manager_status = OktaUsers.get_manager_info(updater)
        board['updater'] = user['last_updated_by']
        board['updater_status'] = updater_status
        board['updater_manager'] = manager
        board['updater_manager_title'] = manager_title
        board['updater_manager_status'] = manager_status
        print("Updator and status: ", updater, updater_status)
    else:
        board['updater'] = ' '
        board['updater_status'] = ' '
        board['updater_manager'] = ' '
        board['updater_manager_title'] = ' '
        board['updater_manager_status'] = ' '

    active_users.append(board)

csv_logic.write_to_file(active_users)
