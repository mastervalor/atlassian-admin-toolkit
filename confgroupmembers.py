import csv
import os
from logic.confluence_logic.groups_logic import ConfGroupLogic

conf_groups = ConfGroupLogic()
group = 'app-confluence'
expand = "status"
newFile = "app-confluence members"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username'])
    while True:
        response = conf_groups.get_group_members_with_status(group, expand)
        if "next" not in response['_links']:
            break
        for member in response['results']:
            if member['status'] == "current":
                writer.writerow([member['username']])
                print(member['username'])
        pref = response['_links']['next']
