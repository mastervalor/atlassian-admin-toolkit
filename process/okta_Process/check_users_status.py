from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='suspended_users')

read_file = os_logic.read_file()

for user in read_file:

    status = OktaUsers.get_user_status(user['email'])
    print(user['email'], status)
