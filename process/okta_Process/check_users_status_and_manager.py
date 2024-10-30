from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker Final List', write_file='looker users')

read_file = os_logic.read_file()
active_users = []

for user in read_file:
    if user['created_by']:
        creator = user['created_by'].replace(' ', '.').lower()
        print(creator)
        # creator_status = OktaUsers.get_user_status(user['created_by'])

    if user['last_updated_by']:
        updater = user['last_updated_by'].replace(' ', '.').lower()
        print(updater)
        # updater_status = OktaUsers.get_user_status(user['last_updated_by'])

        # if creator_status == 'ACTIVE':
        #     active_users.append({
        #         'creator': user['created_by'],
        #         'status': creator_status
        #     })
        #     print(user['created_by'], creator_status)

# os_logic.write_to_file(active_users)
