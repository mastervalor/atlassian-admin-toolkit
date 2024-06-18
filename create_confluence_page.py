from logic.confluence_logic.confluence_space_logic import Spaces

spaces = Spaces()

parent_page = '421062700'
test_page = '588288664'
title = 'table create test from script'
space_key = 'IT'

table_content = """
<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Project Key</th>
      <th>Approver</th>
      <th>Admin Group</th>
      <th>Developer Group</th>
      <th>User Group</th>
      <th>Agent Group</th>
      <th>Project Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Project Apple</td>
      <td>APP</td>
      <td>Tim</td>
      <td>Admins</td>
      <td>Devs</td>
      <td>Users</td>
      <td>Agents</td>
      <td>Software</td>
    </tr>
    <tr>
      <td>Project Banana</td>
      <td>BAN</td>
      <td>Bob</td>
      <td>Admins</td>
      <td>Devs</td>
      <td>Users</td>
      <td>Agents</td>
      <td>Service</td>
    </tr>
    <!-- Add more rows as needed -->
  </tbody>
</table>
"""


response = spaces.create_page(space_key, title, table_content, parent_page)

if response:
    print('Page created successfully:', response)
else:
    print('Failed to create the page.')
