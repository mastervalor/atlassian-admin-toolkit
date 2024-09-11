import os
import csv
from logic.os_logic.os_logic import OSLogic
from logic.jira_logic.user_logic import Users
from logic.jira_logic.groups_users_logic import GroupsUsers
from logic.okta_logic.okta_user_logic import OktaUsers

# Initialize necessary classes
jira_users = Users()
okta_users = OktaUsers()
new_file = 'not in app-jira with status'
open_file = 'not in app-jira'

# Set up the OSLogic instance for reading and writing
os_logic_read = OSLogic(open_file=open_file)
os_logic_write = OSLogic(write_file=new_file, columns=['Username', 'access group', 'status', 'in okta'])

# Read the data from the existing CSV file
csv_data = os_logic_read.read_file()

# Prepare data to be written to the new file
data_to_write = []

for row in csv_data:
    # Get the status of the user from GroupsUsers
    status = jira_users.get_user_status(row['Username'])

    # Get the user ID from OktaUsers
    okta = okta_users.get_user_id(f"{row['Username']}@getcruise.com")
    okta_status = okta['status'] if okta else None

    # Append the data to the list to write later
    data_to_write.append({
        'Username': row['Username'],
        'access group': row['access group'],
        'status': status,
        'in okta': okta_status
    })

    print(f"User {row['Username']} is active: {status} and okta: {okta_status}")

# Write the data to the new file
os_logic_write.write_to_file(data_to_write)