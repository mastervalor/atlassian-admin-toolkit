import csv
import os

mainFile = 'Projects - new_file'
projects = 'Archiving projects plan and times'
newFile = 'final file'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['Name', 'Key', 'Project Type'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), mainFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), projects), mode='r') as new_csv:
                csv_reader2 = csv.DictReader(new_csv)
                if i['Name'] not in [x['Name'] for x in csv_reader2]:
                    writer.writerow([i['Name'], i['key'], i['Project Type']])