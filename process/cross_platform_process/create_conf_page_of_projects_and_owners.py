from logic.confluence_logic.page_logic import Pages
from logic.jira_logic.project_logic import Projects


project = Projects()
page = Pages()
parent_page = '421062700'
title = 'table create test from script three'
space_key = 'IT'
projects_dict = []


projects = project.get_project_owners_and_status()
for row in projects:
    approver = row['username']
    if '[C]' in approver:
        approver = approver.replace('[C]', '')
    row['project'] = html.escape(row['project'])
    row['key'] = html.escape(row['key'])
    row['username'] = html.escape(approver)
    projects_dict.append({
        "project_name": row['project'],
        "project_key": row['key'],
        "approver": row['username'],
        "admin_group": "Admins",
        "developer_group": "Devs",
        "user_group": "Users",
        "agent_group": "Agents",
        "project_type": "Software"
    })

table_headers = ["Project Name", "Project Key", "Approver", "Admin Group", "Developer Group", "User Group",
                 "Agent Group", "Project Type"]

table_content = page.generate_table_content(projects_dict, table_headers)

# Create the Confluence page
response = page.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')
