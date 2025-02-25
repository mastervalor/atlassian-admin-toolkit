import os
import csv
from logic.jira_logic.group_logic import Groups

groups = Groups()
newFile = 'not in app-jira'
openFile = 'groups'

main_group = set(groups.group_members('app-jira'))
missing_list = []

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Username', 'access group'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            response = groups.group_members(i['group_id'])
            if response:
                response = set(response)
                missing = list(response - main_group)
                for user in missing:
                    if user not in missing_list:
                        print("found one: " + user + " in " + i['group_id'])
                        writer.writerow([user, i['group_id']])
                        missing_list.append(user)
                    else:
                        print(user + ' is already in another group, but here is second one, ' + i['group_id'])
                print(missing)
            else:
                print(i['group_id'] + " is empty")
