from call import Okta, call
import json

run = 0
start = 0
total = 50
while start <= total:
    group = call(f'group/member?maxResults=100&startAt={start}', 'members', 'app-jira')
    start += 50
    total = group['total']

print(start)

