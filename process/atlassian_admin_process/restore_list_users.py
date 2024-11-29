from file_manip.csv_file_manip import CSVLogic
from logic.atlassian_admin_logic.user_directory_logic import UserDirectoryLogic

user_directory = UserDirectoryLogic()
csv_logic = CSVLogic(open_file='suspended_active_users')

file = csv_logic.read_file()
user_ids = []

for user in file:
    user_ids.append(str(user['User id']))

user_directory.restore_users(user_ids)
    