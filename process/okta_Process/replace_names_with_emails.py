from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners', write_file='looker owners emails')

file = os_logic.read_file()

for row in file:
    if row['creator']:
        creator = row['creator'].replace(' ', '.')
        creator_email = OktaUsers.get_user_email(creator)

print(OktaUsers.get_user_email('adam.bowser'))
