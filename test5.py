import os, csv
from logic.jira_logic.groups_users_logic import GroupsUsers
from logic.user_logic import Users
from logic.project_logic import Projects
from logic.jira_logic.field_logic import Fields
from call import Jira

groups = GroupsUsers()
projects = Projects()
fields = Fields()
jira = Jira()
users = Users()


# groups.remove_all_group_members("jira-new-hires")
#
openFile = 'jsm users'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        member = users.get_user_applications(row['Username'])
        print(row['Username'], member)
#         project = projects.get_project_type(row['Project Key'])
#         print(project)

# jql = '"Affected Vehicle Track(s)" is not EMPTY'
# results = jira.jql("", jql)
# list = []
# results = projects.get_archived_projects()
# # results = projects.get_project_users_by_role("SIMWEB", "agents")
# for i in results:
#     list.append(i['key'])
#
# for i in list:
#     print(i)
# groups = groups.user_groups('aaron.asbill')
# members = groups.compare_groups('app-jira-agent-license', 'jira-servicedesk-users')
# member = groups.get_user_status('kandice.powell')
# member = groups.get_user_applications('kandice.powell')
# print(member)
# print(json.dumps(member, sort_keys=True, indent=4, separators=(",", ": ")))
