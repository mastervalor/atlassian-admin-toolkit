from call import Jira
import csv
import os

jira = Jira()
openFile = 'owners of done tickets'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        payload = {
            'fields': {
                'project': {
                    'key': 'ITAPP',
                },
                'summary': f"Project key: {row['prject']} lead {row['username']} is no longer with the company",
                "issuetype": {
                        "id": "3"
                },
                "reporter": {
                    "name": "mourad.marzouk"
                 },
                "customfield_28001": {
                    'value': "Jira"
                },
                "description": f"Project key: {row['prject']} lead {row['username']} is no longer with the company "
                               f"and we need to find out who would be the new owner of this project",
            }
        }
        
        jira.create_ticket(payload)