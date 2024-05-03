from logic.groups_users_logic import GroupsUsers
from logic.os_logic import OSLogic
from calls.jira import Jira
import csv, os

os_logic = OSLogic(open_file='jsm users')
groups = GroupsUsers()
jira = Jira()
newFile = 'all jsm users'

app_jira_agent_license = jira.group_members('app-jira-agent-license')
jira_servicedesk_users = jira.group_members('jira-servicedesk-users')
it_Operations = jira.group_members('IT Operations')
jira_administrators = jira.group_members('jira-administrators')
servicedesk = jira.group_members('servicedesk')
file = os_logic.read_file()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(
        ['Directory', 'Username', 'Last Login', 'Assigbing Group', "Status"])
    for row in file:
        status = groups.get_user_status(row['Username'])
        print(f"{row['Username']}:  {status}")
        if row['Username'] in app_jira_agent_license:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'app_jira_agent_license', status])
        elif row['Username'] in jira_servicedesk_users:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'jira_servicedesk_users', status])
        elif row['Username'] in it_Operations:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'it_Operations', status])
        elif row['Username'] in jira_administrators:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'jira_administrators', status])
        elif row['Username'] in servicedesk:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'servicedesk', status])
        else:
            writer.writerow([row['Directory'], row['Username'], row['Last Login'], 'No assigment group', status])
