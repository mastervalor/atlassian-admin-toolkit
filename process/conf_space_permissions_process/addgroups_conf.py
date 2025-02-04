from logic.confluence_logic.space_logic import Spaces
import csv
import os


openFile = 'conflunce role groups and users 2'
space_logic = Spaces()

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for space in csv_reader:
        group = f"okta_confluence_{space['Space key']}_{space['Role']}"
        if space['Role'] == 'editor' or space['Role'] == 'admins':
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'create', 'page')
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'create', 'attachment')
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'create', 'blogpost')
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'create', 'comment')
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with editor rights")
        elif space['Role'] == 'commentor':
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'create', 'comment')
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with commentor rights")
        elif space['Role'] == 'read-only':
            space_logic.set_space_permissions_by_groups_roles(space['Space key'], group, 'read', 'space')
            print(f"Group: {group} in was added to space: {space['Space key']} with read-only rights")
