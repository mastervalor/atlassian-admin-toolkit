from call import Jira
import csv
import os

jira = Jira()
openFile = 'owners of done tickets'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        payload = {

        }
        jira.create_ticket(payload)