from logic.jira_logic.user_logic import Users
import csv
import os


jira_users = Users()
openFile = 'owners of done tickets'
newfile = "Inactive project leads"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username', 'project', 'status'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            status = jira_users.get_user_by_username(i['Project lead'])
            if not status['active']:
                print(i['Project lead'], i['Project Key'], status['active'])
                writer.writerow([i['Project lead'], i['Project Key'], status['active']])
