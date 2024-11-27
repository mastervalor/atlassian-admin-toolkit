from logic.jira_logic.user_logic import Users
from logic.os_logic.csv_logic import CSVLogic

user = Users(is_staging=True)
csv_logic = CSVLogic(open_file='username')
file = csv_logic.read_file()
users = []

for username in file:
    users.append(username['Full name'])

user.delete_list_of_users(users)
