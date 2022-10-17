import csv
import os
import requests
import json
from auth import auth


# url = f"https://lucidmotors-sandbox-693.atlassian.net/rest/api/3/issue/ATLAS-13119"
# headers = {
#     "Accept": "application/json"
# }
#
# response = json.loads(requests.request(
#     "GET",
#     url,
#     headers=headers,
#     auth=auth
# ).text)
#
# project = 'ECR'
#
# if project['key'] in response['fields']['customfield_13510']:
#     print('nope')
# print(response['fields']['customfield_13510'])
# # if 'https' in response['fields']['customfield_13510']:
# #     print("yep I found it")
# # #
# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
# #
# # url_p = "https://lucidmotors.atlassian.net/rest/api/3/project"
# #
# # headers = {
# #     "Accept": "application/json"
# # }
# #
# # response = json.loads(requests.request(
# #     "GET",
# #     url_p,
# #     headers=headers,
# #     auth=auth
# # ).text)
# #
# # projects = []
# #
# # for i in response:
# #     case = {'name': i['name'], 'key': i['key']}
# #     projects.append(case)
# #
# # for project in projects:
# #     print(project['key'])
#
# # def call(pref):
# #     url = f"https://lucidmotors-sandbox-693.atlassian.net/rest/api/3/issue/" + pref
# #     headers = {
# #         "Accept": "application/json"
# #     }
# #
# #     response = json.loads(requests.request(
# #         "GET",
# #         url,
# #         headers=headers,
# #         auth=auth
# #     ).text)
# #
# #     return response
# #
# #
# # response = call('ATLAS-13103')
# # print(response['fields']['summary'])
# # if 'MES' in response['fields']['summary']:
# #     print("found Mes")
# # else:
# #     print("didn't find mes")

# mainFile = 'tickets3'
# total = 1000
# min = 0
# max = 100
#
# with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='w') as new_csv:
#     writer = csv.writer(new_csv)
#     writer.writerow(['Ticket Key'])
#     while max < total:
#         url = f"https://lucidmotors.atlassian.net/rest/api/3/search/?startAt={min}&maxResults={max}"
#         headers = {
#             "Accept": "application/json"
#         }
#
#         query = {
#             'jql': 'project = "SD - Atlassian" AND "Tool[Radio Buttons]" = Jira AND "Jira Project[Project Picker (single project)]" is EMPTY AND summary !~ Automation'
#         }
#
#         response = json.loads(requests.request(
#             "GET",
#             url,
#             headers=headers,
#             params=query,
#             auth=auth
#         ).text)
#         total = response['total']
#         min += 100
#         max += 100
#         print(max, min)
#         for i in response['issues']:
#             print(i['key'])
#             writer.writerow([i['key']])


# def call(ext, groupName='', id=''):
#     url = "https://lucidmotors.atlassian.net/rest/api/3/" + ext
#
#     headers = {
#         "Accept": "application/json"
#     }
#     query = ''
#
#     if groupName:
#         query = {
#             'groupname': groupName
#         }
#     if id:
#         query = {
#             'accountId': id
#         }
#     response = json.loads(requests.request(
#         "GET",
#         url,
#         headers=headers,
#         params=query,
#         auth=auth
#     ).text)
#     return response
#
# emails = []
# x = 'CARE - Developers'
#
# names = call('group/member', x)
# for y in names['values']:
#     email = call('/user', '', y['accountId'])
#     print(email)
#     # emails.append(y['emailAddress'])

# def call(ext, groupName='', id=''):
#     url = "https://lucidmotors.atlassian.net/rest/api/3/" + ext
#
#     headers = {
#         "Accept": "application/json"
#     }
#     query = ''
#
#     if groupName:
#         query = {
#             'groupname': groupName
#         }
#     if id:
#         query = {
#             'accountId': id
#         }
#
#     response = json.loads(requests.request(
#         "GET",
#         url,
#         headers=headers,
#         params=query,
#         auth=auth
#     ).text)
#     return response
#
#
# projectRoles = ['10001', '10002', '10301', '10000', '10300', '10425']
# projectType = ['Developers', 'admins', 'agents', 'users', 'customers', 'suppliers']
#
# for (a, r) in zip(projectRoles, projectType):
#     groupName = call(f'project/CNTRLTEST/role/{a}')
#     for x in groupName['actors']:
#         names = call('group/member', x['displayName'])
#         if 'errorMessages' in names:
#             print(x)
#             user = call('/user', '', x['actorUser']['accountId'])

# mainFile = 'names and tickets'
# openFile = 'name'
# keys = []
#
# with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='w') as new_csv:
#     writer = csv.writer(new_csv)
#     writer.writerow(['Name', 'Ticket Key'])
#     with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), openFile), mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for i in csv_reader:
#             url = "https://lucidmotors.atlassian.net/rest/api/3/search/"
#             headers = {
#                 "Accept": "application/json"
#             }
#
#             query = {
#                 'jql': f'project = "On/Off Boarding" and (summary ~ "Termination Notification – {i["Preferred Name"]}" or summary ~ "Contingent Worker Termination: {i["Preferred Name"]}")'
#             }
#
#             response = json.loads(requests.request(
#                 "GET",
#                 url,
#                 headers=headers,
#                 params=query,
#                 auth=auth
#             ).text)
#             try:
#                 for l in response['issues']:
#                     keys.append(l['key'])
#             except KeyError:
#                 keys.append('none')
#             writer.writerow([i["Preferred Name"], keys])
#             keys.clear()
# url = "https://lucidmotors.atlassian.net/wiki/rest/api/space/ILTS?expand=permissions"
#
# headers = {
#     "Accept": "application/json"
# }
#
# response = json.loads(requests.request(
#     "GET",
#     url,
#     headers=headers,
#     auth=auth
# ).text)
#

# url = f"https://lucidmotors.atlassian.net/rest/api/3/group/bulk"
#
# headers = {
#     "Accept": "application/json"
# }
# query = {
#     'groupname': 'atieva-users'
# }
# response = json.loads(requests.request(
#     "GET",
#     url,
#     headers=headers,
#     params=query,
#     auth=auth
# ).text)


#print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))