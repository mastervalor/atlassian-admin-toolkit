from logic.os_logic.os_logic import OSLogic
from logic.atlassian_admin_logic.user_directory_logic import UserDirectoryLogic

user_directory = UserDirectoryLogic()
os_logic = OSLogic(open_file='suspended_active_users')

file = os_logic.read_file()
user_ids = []

for user in file:
    user_ids.append(str(user['User id']))

user_directory.restore_users(user_ids)
    