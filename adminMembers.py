from call import call
import csv
import os

admins = 'Jira admins copy'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), admins), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        response = call(f'group/member?groupname={i["Group Name"]}', 'get')
        i['Members'] = response['total']
        rows.append(i)
        print(i)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()
