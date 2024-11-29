from logic.jira_logic.user_logic import Users
from file_manip.csv_file_manip import CSVLogic
from logic.jira_logic.group_logic import Groups
import csv, os

csv_logic = CSVLogic(open_file='jsm users')
user = Users()
groups = Groups()
newFile = 'all jsm users'

app_jira_agent_license = groups.group_members('app-jira-agent-license')
jira_servicedesk_users = groups.group_members('jira-servicedesk-users')
it_Operations = groups.group_members('IT Operations')
jira_administrators = groups.group_members('jira-administrators')
servicedesk = groups.group_members('servicedesk')
file = csv_logic.read_file()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(
        ['Directory', 'Username', 'Last Login', 'Assigbing Group', "Status"])
    for row in file:
        status = user.get_user_status(row['Username'])
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
