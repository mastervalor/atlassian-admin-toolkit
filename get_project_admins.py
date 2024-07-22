from logic.project_logic import Projects
from logic.jira_logic.groups_users_logic import GroupsUsers
import os
import csv

projects = Projects()
groups = GroupsUsers()
newFile = 'final owners'
openFile = 'unowned projects'


with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Admins'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            admins = projects.get_project_users_by_role(i['Key'], 'Administrators')
            admins = groups.remove_defult_admins(admins)
            writer.writerow([admins])
            print(i['Key'], admins)
