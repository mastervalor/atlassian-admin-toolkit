from call import call
import csv
import os

file = 'agents'
new_file = 'agent groups'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), new_file), mode='w') as new_writer:
    writer = csv.writer(new_writer)
    writer.writerow(['Username', "Groups"])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), file), mode='r') as new_csv:
        reader = csv.DictReader(new_csv)
        for i in reader:
            username = i['Username'].split('@', 1)[0]
            new = list(set(username.split("\n")))
            username = "\n".join(new)
            response = call("user?expand=groups", 'groups', username)
            groups = []
            try:
                for j in response['groups']['items']:
                    if "-agent" in j['name']:
                        groups.append(j['name'])
            except KeyError:
                groups.append("not groups found")
            print(username)
            writer.writerow([username, groups])
