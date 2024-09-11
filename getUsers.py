from calls.jira import Jira
import csv
import os


jira = Jira()
openFile = 'owners of done tickets'
newfile = "Inactive project leads"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username', 'project', 'status'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            status = jira.get_user(i['Project lead'])
            if not status['active']:
                print(i['Project lead'], i['Project Key'], status['active'])
                writer.writerow([i['Project lead'], i['Project Key'], status['active']])
