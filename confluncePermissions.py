import csv
import os
from group import get_group_users


EDITORS = []
COMMENTORS = []
READ_ONLY = []


def add_perm(group_name, role_name):
    if group_name == "administrators":
        return False
    if (group_name.startswith('cc-') or group_name.startswith('dept-') or
            group_name.startswith('grp-') or group_name.startswith('okta_') or group_name.startswith('division') or
            group_name == 'engineering'):
        if 'page create' in role_name or 'attachment create' in role_name or 'blogpost create' in role_name:
            EDITORS.append(group_name)
        elif 'comment create' in role_name:
            COMMENTORS.append(group_name)
        elif 'space read' in role_name:
            READ_ONLY.append(group_name)
    else:
        emails = get_group_users(group_name)
        for email in emails:
            if 'page create' in role_name or 'attachment create' in role_name or 'blogpost create' in role_name:
                EDITORS.append(email)
            elif 'comment create' in role_name:
                COMMENTORS.append(email)
            elif 'space read' in role_name:
                READ_ONLY.append(email)


user = ''
group = ''
role = []
newFile = 'conflunce role groups and users 2'
openFile = 'spaces_des2'

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['conflunce', 'Space key', 'Role', 'users/Cost Center'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for space in csv_reader:
            response = call(space['Space Key'])
            EDITORS = []
            COMMENTORS = []
            READ_ONLY = []
            group = ''
            role = []
            for i in response['permissions']:
                try:
                    if group == '':
                        group = i['subjects']['group']['results'][0]['name']
                    if i['subjects']['group']['results'][0]['name'] == 'confluence-users':
                        continue
                    if i['subjects']['group']['results'][0]['name'] != 'administrators':
                        if group != i['subjects']['group']['results'][0]['name']:
                            add_perm(group, role)
                            group = i['subjects']['group']['results'][0]['name']
                            role.clear()
                            role.append(i['operation']['targetType'] + ' ' + i['operation']['operation'])
                        elif group == i['subjects']['group']['results'][0]['name']:
                            role.append(i['operation']['targetType'] + ' ' + i['operation']['operation'])
                except KeyError:
                    try:
                        if 'Unlicensed' in i['subjects']['user']['results'][0]['displayName']:
                            print(
                                f"found and inactive users {i['subjects']['user']['results'][0]['displayName']} in the {space['Space Key']}")
                        else:
                            if user != i['subjects']['group']['results'][0]['displayName'] or user == '':
                                user = i['subjects']['group']['results'][0]['displayName']
                                print(space['Space Key'] + ":  displayName   " + user)
                    except KeyError:
                        continue
            add_perm(group, role)
            if EDITORS:
                writer.writerow(['conflunce', space['Space Key'], 'editor', EDITORS])
            if COMMENTORS:
                writer.writerow(['conflunce', space['Space Key'], 'commentor', COMMENTORS])
            if READ_ONLY:
                writer.writerow(['conflunce', space['Space Key'], 'read-only', READ_ONLY])
                writer.writerow(['conflunce', space['Space Key'], 'admins', space['Owners']])
# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
