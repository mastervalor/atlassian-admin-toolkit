from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker Final List', write_file='looker users')

read_file = os_logic.read_file()
active_users = []

for user in read_file:
    board = {'title': user['title']}
    if user['created_by']:
        creator = user['created_by'].replace(' ', '.').lower()
        creator_status = OktaUsers.get_user_status(user['created_by'])
        board['creator'] = user['created_by']
        board['creator_status'] = creator_status

    if user['last_updated_by']:
        updater = user['last_updated_by'].replace(' ', '.').lower()
        updater_status = OktaUsers.get_user_status(user['last_updated_by'])
        board['updater'] = user['last_updated_by']
        board['updater_status'] = updater_status

    active_users.append(board)

os_logic.write_to_file(active_users)
