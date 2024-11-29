from logic.okta_logic.okta_user_logic import OktaUsers
from file_manip.csv_file_manip import CSVLogic

csv_logic = CSVLogic(open_file='looker owners', write_file='looker owners emails')

file = csv_logic.read_file()
user_emails = []

for row in file:
    emails = {}
    if '@' in row['creator']:
        emails['creator'] = row['creator']
    elif row['creator'] == 'None' or not row['creator']:
        emails['creator'] = 'None'
    elif row['creator']:
        creator = row['creator'].replace(' ', '.').lower()
        creator_email = OktaUsers.get_user_email(creator)
        emails['creator'] = creator_email

    if '@' in row['creator_manager']:
        emails['creator_manager'] = row['creator_manager']
    elif row['creator_manager'] == 'None' or not row['creator_manager']:
        emails['creator_manager'] = 'None'
    elif row['creator_manager']:
        manager_email = OktaUsers.get_user_email(row['creator_manager'])
        emails['creator_manager'] = manager_email

    if '@' in row['updater']:
        emails['updater'] = row['updater']
    elif row['updater'] == 'None' or not row['updater']:
        emails['updater'] = 'None'
    elif row['updater']:
        updater = row['updater'].replace(' ', '.').lower()
        updater_email = OktaUsers.get_user_email(updater)
        emails['updater'] = updater_email

    if '@' in row['updater_manager']:
        emails['updater_manager'] = row['updater_manager']
    elif row['updater_manager'] == 'None' or not row['updater_manager']:
        emails['updater_manager'] = 'None'
    elif row['updater_manager']:
        updater_manager_email = OktaUsers.get_user_email(row['updater_manager'])
        emails['updater_manager'] = updater_manager_email

    user_emails.append(emails)

csv_logic.write_to_file(user_emails)
