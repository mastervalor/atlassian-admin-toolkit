from logic.os_logic import OSLogic
from logic.groups_users_logic import GroupsUsers

os_logic = OSLogic(open_file='learn agents', write_file='learn agents groups')
groups = GroupsUsers()
file = os_logic.read_file()

os_logic.append_file(["learn agents", "other groups"])

for name in file:
    user_group = groups.user_groups(name['LEARN agents '])
    agent_groups = [group for group in user_group if group.endswith("-agent")]
    os_logic.append_file({"learn agents": name['LEARN agents '], "other groups": agent_groups})

