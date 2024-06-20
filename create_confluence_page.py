from logic.confluence_logic.page_logic import Pages
from logic.os_logic import OSLogic
from project_info_with_owners_and_groups import project_info
import html
import logging

page = Pages()

projects = project_info()
parent_page = '421062700'
# test_page = '588288664'
title = 'table create test from script three'
space_key = 'IT'
projects_dict = []

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

# Define the table headers
table_headers = ["Project Name", "Project Key", "Approver", "Admin Group", "Developer Group", "User Group",
                 "Agent Group", "Project Type"]

table_content = page.generate_table_content(projects_dict, table_headers)

# Create the Confluence page
response = page.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')