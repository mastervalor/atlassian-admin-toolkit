from logic.jira_logic.user_logic import Users
from logic.os_logic.os_logic import OSLogic

user = Users(is_staging=True)
os_logic = OSLogic(open_file='username')
file = os_logic.read_file()
users = []

for username in file:
    users.append(username['Full name'])

user.delete_list_of_users(users)

