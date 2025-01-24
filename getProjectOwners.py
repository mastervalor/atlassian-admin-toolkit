import os
import csv
from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls

projects = ProjectJiraCalls()
newFile = 'final owners'
openFile = 'unowned projects'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Owner'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            owner = projects.project_owner(i['Key'])
            writer.writerow([owner[0]])
            print(owner[0])
