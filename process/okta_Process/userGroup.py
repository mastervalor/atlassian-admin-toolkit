from logic.os_logic.csv_logic import CSVLogic
from logic.jira_logic.group_logic import Groups
from logic.jira_logic.user_logic import Users

columns = ["learn agents", "other groups"]

csv_logic = CSVLogic(open_file='learn agents', append_file='learn agents groups', columns=columns)
groups = Groups()
users = Users()
file = csv_logic.read_file()

for name in file:
    user_group = users.user_groups(name['LEARN agents '])
    agent_groups = [group for group in user_group if group.endswith("-agent")]
    csv_logic.append_to_file([name['LEARN agents '], agent_groups])
