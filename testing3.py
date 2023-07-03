from call import Okta, call, Confluence, Jira
import json
import requests
from auth import conf_token
from config import confluence
import csv
import os

# run = 0
# start = 0
# total = 50
# while start <= total:
#     group = call(f'group/member?maxResults=100&startAt={start}', 'members', 'app-jira')
#     start += 50
#     total = group['total']
#
# print(start)

# call = Confluence.user_search()
# print(json.dumps(call, sort_keys=True, indent=4, separators=(",", ": ")))

# newFile = "Group Match"
# openFile = "app-confluence members"
#
# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
#     writer = csv.writer(new_csv)
#     writer.writerow(['Username', 'groups not in okta'])
# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for user in csv_reader:


# response = Confluence.user_groups("mourad.marzouk")
# for i in response['results']:
#     print(i['name'])

# response = call('project/WV', 'get')
#
# print(response['lead']['name'])

jira = Jira()
tickets = jira.jql('?startAt=0&maxResults=1000', 'updatedDate <= startOfDay(-730d) and statusCategory = Done')

print(json.dumps(tickets, sort_keys=True, indent=4, separators=(",", ": ")))
