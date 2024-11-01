from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners')

file = os_logic.read_file()

print(OktaUsers.get_user_email('adam.bowser'))
