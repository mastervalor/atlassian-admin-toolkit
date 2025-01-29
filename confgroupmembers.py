import json
import csv
import os
from calls.confluence_api_calls.conf_api_groups import ConfluenceGroupsCalls

conf_groups = ConfluenceGroupsCalls()
pref = "/rest/api/group/app-confluence/member?expand=status"
newFile = "app-confluence members"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['username'])
    while True:
        response = conf_groups.group_members(pref)
        if "next" not in response['_links']:
            break
        for member in response['results']:
            if member['status'] == "current":
                writer.writerow([member['username']])
                print(member['username'])
        pref = response['_links']['next']
