from logic.groups_users_logic import GroupsUsers
from logic.os_logic import OSLogic
from calls.jira import Jira

os_logic = OSLogic(open_file='jsm users')
groups = GroupsUsers()
jira = Jira()

app_jira_agent_license = jira.group_members('app-jira-agent-license')
jira_servicedesk_users = jira.group_members('jira-servicedesk-users')
it_Operations = jira.group_members('IT Operations')
jira_administrators = jira.group_members('jira-administrators')
servicedesk = jira.group_members('servicedesk')


file = os_logic.read_file()
for i in file:
    print(i['Username'])

#next loop through the sheet and get all their status and check what group they are from.