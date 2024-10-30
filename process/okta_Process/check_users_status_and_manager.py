from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker Final List', write_file='looker users')

read_file = os_logic.read_file()
active_users = []

for user in read_file:
    if user['User status'] == 'Suspended':
        if user['created_by']:
            creator_status = OktaUsers.get_user_status(user['created_by'])
            if creator_status == 'ACTIVE':
                active_users.append({
                    'User id': user['User id'],
                    'Email': user['email'],
                    'Name': user['User name'],
                    'status': creator_status
                })
                print(user['email'], creator_status)

        if user['last_updated_by']:
            updater_status = OktaUsers.get_user_status(user['last_updated_by'])
            if updater_status == 'ACTIVE':
                active_users.append({
                    'User id': user['User id'],
                    'Email': user['email'],
                    'Name': user['User name'],
                    'status': updater_status
                })
                print(user['email'], updater_status)

os_logic.write_to_file(active_users)
