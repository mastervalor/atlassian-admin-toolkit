import json
from call import call, staging_call


components = call('project/SEC/components', 'get')


for component in components:
    payload = json.dumps({
        "name": component['name'],
        "description": component['description'] if 'description' in component else "",
        "leadUserName": component['lead']['displayName'] if 'lead' in component else "",
        "assigneeType": component['assigneeType'],
        "isAssigneeTypeValid": component['isAssigneeTypeValid'],
        "project": "THREAT",
        "projectId": 26904
    })
    call('component', 'post', payload)


print(json.dumps(components, sort_keys=True, indent=4, separators=(",", ": ")))