from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic
import re

os_logic = OSLogic(open_file='Jira API Integration Tokens Inventory', write_file='Jira API Tokens Inventory completed')
file = os_logic.read_file()

for row in file:
    if not row['Owner']:
        svc = re.search(r'\((.*?)\)', row['API Integration Account']).group(1)
        owner = OktaUsers.get_user_second_email(svc)
        owner_status = OktaUsers.get_user_status(owner)
        print(owner, owner_status)
