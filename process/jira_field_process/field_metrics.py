import csv
import os
from logic.jira_logic.field_logic import Fields

fields = Fields()
newFile = 'field metrics'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['Field name', 'Field type', 'Locked field', 'Global only', 'Projects', 'Screens', 'Issues', "Notes"])
    metrics = fields.field_metrics()
    for i in metrics:
        if 'notes' in i:
            writer.writerow(
                [i['name'], i['type'], i['isLocked'], i['isAllProjects'], i['projectsCount'], i['screensCount'],
                 "Can't find", i['notes']])
        else:
            writer.writerow(
                [i['name'], i['type'], i['isLocked'], i['isAllProjects'], i['projectsCount'], i['screensCount'],
                 i['issuesWithValue'], ""])
# print(json.dumps(fields, sort_keys=True, indent=4, separators=(",", ": ")))
