from logic.os_logic import OSLogic
from logic.groups_users_logic import GroupsUsers

os_logic = OSLogic(open_file='learn agents', write_file='learn agents groups')
groups = GroupsUsers()

file = os_logic.read_file()

for name in file:
    group = groups.user_groups(name['LEARN agents '])
    print(group)
