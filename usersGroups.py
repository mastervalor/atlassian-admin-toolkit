from call import call
import csv
import os


file = 'agents'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), file), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        username = i['email'].split("@")[0]
        response = call("user?expand=groups", 'groups', username)
        groups = []
        try:
            for j in response['groups']['items']:
                if "-agent" in j['name']:
                    groups.append(j['name'])
        except KeyError:
            rows.append(i)
        i['groups'] = groups
        rows.append(i)
        print(username)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()
