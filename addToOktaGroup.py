import os
import csv
from call import Okta

openFile = 'not in app-jira'
group_id = Okta.get_group_id('app-jira')
newFile = 'updated missing members'
addedFile = 'members added'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), addedFile), mode='w') as added:
        writer2 = csv.writer(added)
        writer2.writerow(['Username', 'access group', 'id', 'status'])
        with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
            writer = csv.writer(new_csv)
            writer.writerow(['Username', 'access group', 'status'])
            for row in csv_reader:
                user = Okta.users_id(row['Username'] + '@getcruise.com')
                if user is False:
                    writer.writerow([row['Username'], row['access group'], 'Not in okta'])
                    print(f"couldn't find {row['Username']}")
                elif user['status'] == 'DEPROVISIONED':
                    writer.writerow([row['Username'], row['access group'], 'DEPROVISIONED'])
                    print(f"{row['Username']} is no longer active")
                else:
                    response = Okta.add_user_to_group(user['id'], group_id)
                    writer2.writerow([row['Username'], row['access group'], user['id'], "added to app-jira"])
                    print(f"{row['Username']} is active and their id is {user['id']}, status of add: {response}")