from logic.project_logic import Projects
import os
import csv

projects = Projects()
newFile = 'final owners'
openFile = 'unowned projects'
admins = []

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Admins'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            projects.get_project_users_by_role(i['Key'], 'Administrators')
