from logic.confluence_logic.page_logic import Pages

page = Pages()

parent_page = '421062700'
test_page = '588288664'
title = 'table create test from script'
space_key = 'IT'

projects_dict = [
    {
        "project_name": "Project Apple",
        "project_key": "APP",
        "approver": "Tim",
        "admin_group": "Admins",
        "developer_group": "Devs",
        "user_group": "Users",
        "agent_group": "Agents",
        "project_type": "Software"
    },
    {
        "project_name": "Project Banana",
        "project_key": "BAN",
        "approver": "Bob",
        "admin_group": "Admins",
        "developer_group": "Devs",
        "user_group": "Users",
        "agent_group": "Agents",
        "project_type": "Service"
    }
    # Add more projects as needed
]

# Define the table headers
table_headers = ["Project Name", "Project Key", "Approver", "Admin Group", "Developer Group", "User Group",
                 "Agent Group", "Project Type"]

table_content = page.generate_table_content(projects_dict, table_headers)


response = page.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')
