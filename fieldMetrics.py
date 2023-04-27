import csv
import os
import json
from call import field_metrics, call
import urllib.parse

fields = field_metrics()
newFile = 'field metrics'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['Field name', 'Field type', 'Locked field', 'Global only', 'Projects', 'Screens', 'Issues', "Notes"])
    for i in fields['values']:
        if 'issuesWithValue' in i:
            writer.writerow([i['name'], i['type'], i['isLocked'], i['isAllProjects'], i['projectsCount'], i['screensCount'], i['issuesWithValue'], ""])
        else:
            jql = '"' + i['name'] + '" is not EMPTY'
            encoded = urllib.parse.quote(jql)
            try:
                results = call(encoded, 'search')
                writer.writerow([i['name'], i['type'], i['isLocked'], i['isAllProjects'], i['projectsCount'], i['screensCount'], results['total'], ''])
            except KeyError:
                print(i['name'], results['errorMessages'])
                writer.writerow(
                    [i['name'], i['type'], i['isLocked'], i['isAllProjects'], i['projectsCount'], i['screensCount'], "Can't find", results['errorMessages']])

# print(json.dumps(fields, sort_keys=True, indent=4, separators=(",", ": ")))
