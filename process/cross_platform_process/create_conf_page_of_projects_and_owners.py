from logic.confluence_logic.page_logic import Pages
from logic.jira_logic.project_logic import Projects
import html


project = Projects()
page = Pages()
parent_page = '421062700'
title = 'table create test from script 5'
space_key = 'IT'
projects_dict = []


projects = project.get_project_owners_and_status()
for row in projects:
    row['project'] = html.escape(row['project'])
    row['key'] = html.escape(row['key'])
    admins = project.get_project_admins_group(row['Key'])
    if row['Project type'] == 'software':
        developers = project.get_project_developer_group(row['Key'])
    elif row['Type'] == 'service_desk':

    projects_dict.append({
        "project_name": row['Project'],
        "project_key": row['Key'],
        "owner": row['Name'],
        "admin_group": admins,
        "developer_group": row['Developer group'],
        "user_group": row['User group'],
        "agent_group": row['Agent group'],
        "project_type": row['Type']
    })

table_headers = ["Project Name", "Project Key", "Approver/Owner", "Admin Group", "Developer Group", "User Group",
                 "Agent Group", "Project Type"]

table_content = page.generate_table_content(projects_dict, table_headers)

# Create the Confluence page
response = page.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')
