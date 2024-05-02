from logic.groups_users_logic import GroupsUsers
from logic.os_logic import OSLogic
from calls.jira import Jira

os_logic = OSLogic(open_file='jsm users')
groups = GroupsUsers()
jira = Jira()

app_jira_agent_license = []
jira_servicedesk_users = []
it_Operations = []
jira_administrators = []


file = os_logic.read_file()
for i in file:
    print(i['Username'])
