from calls.jira_api_calls.jira_api_user_calls import UserJiraCalls
import json

user = UserJiraCalls()
permission_key = "CREATE_ISSUE"

data = user.get_my_permissions()

if permission_key in data['permissions']:
        permission_info = data['permissions'][permission_key]
        if permission_info['havePermission']:
            # You have the specified permission
            projects_with_permission = [
                project['name'] for project in permission_info['projects']
            ]
            if projects_with_permission:
                print(f"You have '{permission_key}' permission in the following projects:")
                for project_name in projects_with_permission:
                    print(project_name)
            else:
                print("You have the permission, but it's not associated with any projects.")
        else:
            # You don't have the specified permission
            print(f"You do not have '{permission_key}' permission.")
else:
    print(f"Permission '{permission_key}' not found in the response.")
