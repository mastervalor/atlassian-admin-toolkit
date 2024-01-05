from call import Jira
import csv
import os


jira = Jira()
newfile = "Inactive project leads"
projects = jira.get_projects_with_owners()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username', 'project', 'key', 'status'])
    for project in projects:
        if not project['lead']['active']:
            writer.writerow([project['lead']['name'], project['name'], project['key'], project['lead']['active']])
