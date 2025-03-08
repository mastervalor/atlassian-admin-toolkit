import csv
import os
from
from call import call, project_metric

newFile = 'Projects metrics'
response = call('project', 'get')
projects = {}

for i in response:
    projects[i['key']] = [i['name'], i['projectTypeKey'], i['id']]

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(
        ['Name', 'key', 'Project Type', 'Project Id', 'Total Tickets', 'Last ticket', 'Last ticket creation date',
         'Earliest ticket', "Earliest ticket creation date"])

    for key in projects:
        project = project_metric(key)
        for l in project:
            projects[key].append(l)
        if projects[key][3] == 0:
            writer.writerow(
                [projects[key][0], key, projects[key][1], projects[key][2], projects[key][3], projects[key][4]])
        else:
            writer.writerow([projects[key][0], key, projects[key][1], projects[key][2], projects[key][3],
                             projects[key][4], projects[key][5], projects[key][6], projects[key][7]])
