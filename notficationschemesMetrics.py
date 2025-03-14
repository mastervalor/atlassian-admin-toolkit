from call import call
from logic.jira_logic.system_logic import JiraSystemsLogic

jira_system = JiraSystemsLogic()

response = call('permissionscheme', 'get')


for i in response['permissionSchemes']:
    print(i['name'])

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))