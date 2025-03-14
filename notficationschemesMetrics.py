from logic.jira_logic.system_logic import JiraSystemsLogic

jira_system = JiraSystemsLogic()

permission_schemes = jira_system.get_all_permission_schemes()


for permission_scheme in permission_schemes['permissionSchemes']:
    print(permission_scheme['name'])

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))