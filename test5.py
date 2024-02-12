import os, csv
from logic.groups_users_logic import GroupsUsers
from logic.project_logic import Projects

groups = GroupsUsers()
projects = Projects()

# groups.remove_all_group_members("jira-new-hires")

openFile = 'projects'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        project = projects.get_project_type(row['Project Key'])
        print(project)
# print(json.dumps(project, sort_keys=True, indent=4, separators=(",", ": ")))