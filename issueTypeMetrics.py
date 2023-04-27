from call import call
import csv
import os
import urllib.parse

page = "issue types"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), page), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'Ticket count'])
    results = call('issuetype', 'get')
    for i in results:
        encoded = urllib.parse.quote(i['name'])
        search = call(f'issuetype="{encoded}"', 'search')
        try:
            total = search['total']
            print(i['name'], total)
            writer.writerow([i['name'], total])
        except KeyError:
            print(i['name'])
            writer.writerow([i['name'], 'Sub-Task', 0])

# print(json.dumps(results, sort_keys=True, indent=4, separators=(",", ": ")))