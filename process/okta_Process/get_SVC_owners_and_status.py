from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic


okta_logic = OktaUsers()
os_logic = OSLogic(open_file='Jira API Integration Tokens Inventory', write_file='Jira API Tokens Inventory completed')
file = os_logic.read_file()

for row in file:
    if row['Owner']:
        print(row['Owner'])
