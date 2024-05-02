from logic.groups_users_logic import GroupsUsers
from logic.os_logic import OSLogic

os_logic = OSLogic(open_file='jsm users')
groups = GroupsUsers()

file = os_logic.read_file()
for i in file:
    print(i['Username'])
