from logic.confluence_logic.page_logic import Pages
from project_info_with_owners_and_groups import project_info
import html

page = Pages()

projects = project_info()
parent_page = '421062700'
# test_page = '588288664'
title = 'table create test from script four'
space_key = 'IT'
projects_dict = []

for row in projects:
    approver = row['Approver']
    if '[C]' in approver:
        approver = approver.replace('[C]', '')
    if '[GM]' in approver:
        approver = approver.replace('[GM]', '')

    row['Name'] = html.escape(row['Name'])
    row['key'] = html.escape(row['Key'])
    row['username'] = html.escape(approver)
    projects_dict.append({
        "project_name": row['Name'],
        "project_key": row['key'],
        "approver": row['username'],
        "admin_group": row['Admin group'],
        "developer_group": row['Developer group'],
        "user_group": row['User group'],
        "agent_group": row['Agent group'],
        "project_type": row['Project type']
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