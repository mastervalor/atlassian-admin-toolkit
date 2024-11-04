from logic.okta_logic.okta_user_logic import OktaUsers
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='looker owners', write_file='looker owners emails')

file = os_logic.read_file()

for row in file:
    if row['creator']:
        creator = row['creator'].replace(' ', '.')
        creator_email = OktaUsers.get_user_email(creator)
        if creator_email is None:
            print(f'Could not find creator: {creator}')

    if row['creator_manager']:
        manager_email = OktaUsers.get_user_email(row['creator_manager'])
        if manager_email is None:
            print(f"Could not find creator's manager: {row['creator_manager']}")

    if row['updater']:
        updater = row['updater'].replace(' ', '.')
        updater_email = OktaUsers.get_user_email(updater)
        if updater_email is None:
            print(f'Could not find updater: {updater}')

    if row['updater_manager']:
        manager_email = OktaUsers.get_user_email(row['updater_manager'])
        if manager_email is None:
            print(f"Could not find updater manager: {row['updater_manager']}")


print(OktaUsers.get_user_email('adam.bowser'))
