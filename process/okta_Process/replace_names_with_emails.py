from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners', write_file='looker owners emails')

file = os_logic.read_file()
user_emails = {}

for row in file:
    if row['creator'] and '@' not in row['creator'] and row['creator'] != 'None':
        creator = row['creator'].replace(' ', '.').lower()
        creator_email = OktaUsers.get_user_email(creator)

    if row['creator_manager'] and '@' not in row['creator_manager'] and row['creator_manager'] != 'None':
        manager_email = OktaUsers.get_user_email(row['creator_manager'])

    if row['updater'] and '@' not in row['updater'] and row['updater']  != 'None':
        updater = row['updater'].replace(' ', '.').lower()
        updater_email = OktaUsers.get_user_email(updater)

    if row['updater_manager'] and '@' not in row['updater_manager'] and row['updater_manager']  != 'None':
        manager_email = OktaUsers.get_user_email(row['updater_manager'])

