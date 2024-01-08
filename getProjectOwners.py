import os
import csv
from call import Jira

jira = Jira()
newFile = 'final owners'
openFile = 'unowned projects'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Owner'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            owner = jira.project_owner(i['Key'])
            writer.writerow([owner[0]])
            print(owner[0])
