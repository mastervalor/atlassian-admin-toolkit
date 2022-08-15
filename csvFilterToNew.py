import csv
import os

mainFile = 'Emads org'
projects = 'projects'
newFile = 'final file'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='a') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['Owner', 'Project'])
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), projects), mode='r') as new_csv:
            csv_reader = csv.DictReader(new_csv)
            for x in csv_reader:
                if i['Owner'].lower() == x['Project Owner'].lower():
                    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='a') as csv_writing:
                        writer = csv.writer(csv_writing)
                        writer.writerow([x['Project Owner'], x['Project Name']])