import csv
import os

mainFile = 'Atlassian Audit Export'
oktaFile = 'Export Users 2022-03-03 01-35-02'
newFile = 'inactive users'

email = ''
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='a') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'Email', 'Start date', 'Last seen on service management',
                     'Last seen on Jira software', 'Last seen on Confluence', 'Title', 'Manager'])
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        email = i['email']
        with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), oktaFile), mode='r') as csv_files:
            csv_readers = csv.DictReader(csv_files)
            for t in csv_readers:
                if email == t['Primary email'].lower():
                    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='a') as new_csv:
                        writer = csv.writer(new_csv)
                        writer.writerow([i['User name'], i['email'], i['Added to org'],
                                         i['Last seen in Jira Service Management - lucidmotors'],
                                         i['Last seen in Jira Software - lucidmotors'],
                                         i['Last seen in Confluence - lucidmotors'], t['Title'], t['Manager']])
                        print(i['email'], t['Title'])
