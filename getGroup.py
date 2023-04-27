import json
from call import call

start = 0
total = 50
active = 0
inactive = 0
while start <= total:
    response = call(f'group/member?groupname=app-jira&startAt={start}', 'get')
    for i in response['values']:
        if i['active'] is True:
            active += 1
        elif i['active'] is False:
            inactive += 1
    start += 50
    total = response['total']

print(active)
print(inactive)

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

