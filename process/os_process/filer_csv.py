import csv
import os

mainFile = 'InactiveUsers'
newFileN = 'Inactive Never accessed'
newFileE = 'Inactive email'

email = ''
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFileE), mode='a') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'Days since Account Created', 'Last seen on service management', 'Days since JSM Access',
                     'Last seen on Jira software', 'Days Since Jira Access', 'Last seen on Confluence',
                     'Days Since Confluence Access', 'Title', 'Manager'])
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFileN), mode='a') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'Days since Account Created', 'Last seen on service management', 'Days since JSM Access',
                     'Last seen on Jira software', 'Days Since Jira Access', 'Last seen on Confluence',
                     'Days Since Confluence Access', 'Title', 'Manager'])
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        if 'Director' not in i['Title']:
            if 'Manager' not in i['Title']:
                if 'Never Accessed' in i['Last seen in Jira Service Management - lucidmotors'] and \
                        'Never Accessed' in i['Last seen in Jira Software - lucidmotors'] and \
                        'Never Accessed' in i['Last seen in Confluence - lucidmotors']:
                    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFileN), mode='a') as new_csv:
                        writer = csv.writer(new_csv)
                        writer.writerow([i['Emial'], i['Days since Account Created'],
                                         i['Last seen in Jira Service Management - lucidmotors'], i['Days since JSM Access'],
                                         i['Last seen in Jira Software - lucidmotors'], i['Days Since Jira Access'],
                                         i['Last seen in Confluence - lucidmotors'], i['Days Since Confluence Access'],
                                         i['Title'], i['Manager']])
                        print(i['Emial'], i['Title'])
                else:
                    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFileE), mode='a') as new_csv:
                        writer = csv.writer(new_csv)
                        writer.writerow([i['Emial'], i['Days since Account Created'],
                                         i['Last seen in Jira Service Management - lucidmotors'], i['Days since JSM Access'],
                                         i['Last seen in Jira Software - lucidmotors'], i['Days Since Jira Access'],
                                         i['Last seen in Confluence - lucidmotors'], i['Days Since Confluence Access'],
                                         i['Title'], i['Manager']])
                        print(i['Emial'], i['Title'])
