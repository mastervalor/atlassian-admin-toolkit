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
    approver = row['Name']
    row['Project'] = html.escape(row['Project'])
    row['Key'] = html.escape(row['Key'])
    row['username'] = html.escape(approver)
    admins = project.get_project_admins_group(row['Key'])
    users = project.get_project_users_group(row['Key'])
    agents = ''
    developers = ''
    if row['Type'] == 'software':
        developers = project.get_project_developers_group(row['Key'])
    elif row['Type'] == 'service_desk':
        agents = project.get_project_agents_group(row['Key'])

    projects_dict.append({
        "project_name": row['Project'],
        "project_key": row['Key'],
        "owner": row['username'],
        "admin_group": admins,
        "developer_group": developers,
        "user_group": users,
        "agent_group": agents,
        "project_type": row['Type']
    })

table_headers = ["Project Name", "Project Key", "Owner", "Admin Group", "Developer Group", "User Group",
                 "Agent Group", "Project Type"]

table_content = page.generate_table_content(projects_dict, table_headers)

# Create the Confluence page
response = page.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')
