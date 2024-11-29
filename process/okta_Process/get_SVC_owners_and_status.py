from logic.okta_logic.okta_user_logic import OktaUsers
from file_manip.csv_file_manip import CSVLogic
import re

csv_logic = CSVLogic(open_file='Jira API Integration Tokens Inventory', write_file='Jira API Tokens Inventory completed')
file = csv_logic.read_file()
accounts = []

for row in file:
    if not row['Owner']:
        svc = re.search(r'\((.*?)\)', row['API Integration Account']).group(1)
        owner = OktaUsers.get_user_second_email(svc)
        if owner:
            owner_status = OktaUsers.get_user_status(owner)
            if owner_status == 'DEPROVISIONED':
                manager = OktaUsers.get_user_manager(owner)
                if manager:
                    manager_status = OktaUsers.get_user_status(manager)
                    print(row['API Integration Account'], owner, owner_status, manager, manager_status)
                else:
                    print(row['API Integration Account'], owner, owner_status, manager)
            else:
                print(row['API Integration Account'], owner, owner_status)
        else:
            print(row['API Integration Account'], owner)
