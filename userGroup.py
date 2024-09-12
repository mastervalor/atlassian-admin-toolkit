from logic.os_logic import OSLogic
from logic.jira_logic.group_logic import GroupsUsers
from logic.jira_logic.user_logic import Users

columns = ["learn agents", "other groups"]

os_logic = OSLogic(open_file='learn agents', append_file='learn agents groups', columns=columns)
groups = GroupsUsers()
users = Users()
file = os_logic.read_file()

for name in file:
    user_group = users.user_groups(name['LEARN agents '])
    agent_groups = [group for group in user_group if group.endswith("-agent")]
    os_logic.append_to_file([name['LEARN agents '], agent_groups])
