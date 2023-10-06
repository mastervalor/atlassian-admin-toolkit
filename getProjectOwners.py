import os
import csv
from call import Jira

jira = Jira()
newFile = 'full projects list'
openFile = 'final file'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'Key', 'Project Type', 'Owner'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            jira.get_project(i['Key'])
