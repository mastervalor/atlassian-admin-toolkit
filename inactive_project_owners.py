from logic.project_logic import Projects
import csv
import os


project = Projects()
newfile = "Inactive project leads"
projects = project.get_project_owners_and_status()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username', 'project', 'key', 'status'])
    for project in projects:
        if not project['lead']['active']:
            writer.writerow([project['lead']['name'], project['name'], project['key'], project['lead']['active']])
