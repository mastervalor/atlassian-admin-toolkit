from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker Final List', write_file='looker users')

read_file = os_logic.read_file()
active_users = []

for user in read_file:
    if user['User status'] == 'Suspended':
        status = OktaUsers.get_user_status(user['email'])
        if status == 'ACTIVE':
            active_users.append({
                'User id': user['User id'],
                'Email': user['email'],
                'Name': user['User name'],
                'status': status
            })
            print(user['email'], status)

os_logic.write_to_file(active_users)
