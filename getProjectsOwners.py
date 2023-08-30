from call import Jira
import csv
import os

jira = Jira()
openFile = 'Archiving projects plan and times'
newFile = 'with owners'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(
        ['Name', 'Key', 'Project Type', 'Project Id', 'Total Tickets', 'Last ticket', 'Last ticket creation date',
         'Earliest ticket', 'Earliest ticket creation date', "Owner", 'Owner Active', 'Project Status'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            manager = jira.project_owner(row['key'])
            print(manager)
            writer.writerow([row['Name'], row['key'], row['Project Type'], row['Project Id'], row['Total Tickets'],
                             row['Last ticket'], row['Last ticket creation date'], row['Earliest ticket'],
                             row['Earliest ticket creation date'], manager[0], manager[1], 'Active'])

