import csv
import os

mainFile = 'Confluence Page Analytics'
newFile2 = 'user_export'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile2), mode='a') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['title', 'cost center', 'manager'])

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        if 'Never Accessed' in i['Last seen in Jira Service Management - lucidmotors'] and \
                'Never Accessed' in i['Last seen in Jira Software - lucidmotors'] and \
                'Never Accessed' in i['Last seen in Confluence - lucidmotors']:
            with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile2), mode='a') as new_csv:
                writer = csv.writer(new_csv)
                writer.writerow([i['Email'], i['Days since Account Created'],
                                 i['Last seen in Jira Service Management - lucidmotors'], i['Days since JSM Access'],
                                 i['Last seen in Jira Software - lucidmotors'], i['Days Since Jira Access'],
                                 i['Last seen in Confluence - lucidmotors'], i['Days Since Confluence Access'],
                                 i['Title'], i['Manager']])
                print(i['Emial'], i['Title'])
        else:
            with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFileE), mode='a') as new_csv:
                writer = csv.writer(new_csv)
                writer.writerow([i['Email'], i['Days since Account Created'],
                                 i['Last seen in Jira Service Management - lucidmotors'], i['Days since JSM Access'],
                                 i['Last seen in Jira Software - lucidmotors'], i['Days Since Jira Access'],
                                 i['Last seen in Confluence - lucidmotors'], i['Days Since Confluence Access'],
                                 i['Title'], i['Manager']])
                print(i['Emial'], i['Title'])