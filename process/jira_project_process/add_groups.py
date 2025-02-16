from logic.jira_logic.project_logic import Projects

projectRoles = ['10001', '10002', '10301', '10000', '10300', '10425', '10432']
projectType = ['developers', 'admins', 'agents', 'users', 'customers', 'suppliers', 'read-only']
project_logic = Projects()
project_keys = project_logic.get_active_all_project_keys()

for i in project_keys:
    for (t, l) in zip(projectType, projectRoles):
        group = f'okta_jira_{i["key"]}_{t}'
        response = project_logic.add_group_to_project_by_role(group, l, i['key'])
        if response.status_code == 200:
            print(f"This group: {group}, was added to project: {i['key']} with the role of {t}")
        elif response.status_code == 400:
            print(f"This group: {group}, did not match to project: {i['key']} with the role of {t}")
        else:
            print(response)
