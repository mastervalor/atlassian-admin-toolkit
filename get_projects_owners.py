from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls
import csv
import os

jira = ProjectJiraCalls()
openFile = 'final file'
newFile = 'with owners'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(
        ['Name', 'Key', 'Project Type', 'Owner Name', 'Owner Active', 'Project Status',
         'Resolution scheme', 'Permission Scheme', 'Notifications Scheme', 'Priority scheme'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['Key'])
            manager = jira.project_owner(row['Key'])
            print(manager)
            writer.writerow([row['Name'], row['Key'], row['Project Type'], manager[0], manager[1],
                             'Active', 'Standard'])
