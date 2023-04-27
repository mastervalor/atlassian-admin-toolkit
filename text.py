import csv
import os
import requests
import json
from call import call, project_metric, Okta, conf_call, field_metrics
from auth import auth, okta_token,  conf_token


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


# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
#
# url = "https://jira.robot.car/rest/api/2/project/EMSTOP"
# headers = {
#         "Accept": "application/json"
#     }
# response = requests.request(
#         "GET",
#         url,
#         headers=headers,
#         auth=auth
#     )
#
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# response = call('project?expand=lead', 'get')
# response = call('attachment/744476', 'get')

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

# Set up variables for Okta API request
# url = 'https://cruise.okta.com/api/v1/users'
# email = 'trivender.dalal@getcruise.com'
# params = {'filter': 'profile.email eq "{0}"'.format(email)}
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': 'SSWS 00erjLWtoLWQPT5Hppge3gnMnDSZp0mcEtBRdoAV1W'
# }
#
# # Make the Okta API request
# response = requests.get(url, headers=headers, params=params)
# print(json.loads(response.text)[0]['profile']['manager'])
# if response.status_code == 200:
#     # Parse the response as JSON
#     response_json = json.loads(response.text)
#
#     # If there is at least one user returned, print their profile
#     if len(response_json) > 0:
#         user = response_json[0]
#         print('User found:')
#         print(json.dumps(user, indent=4))
#     else:
#         print('No users found with email: ' + email)
# else:
#     print('Error searching for user: ' + str(response.status_code))

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# res = call('group/member?groupname=app-fira-FCI-administrator', 'get')
# print(res)

# admins = 'Jira admins copy'
#
# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), admins), mode='r+') as new_csv:
#     reader = csv.DictReader(new_csv)
#     writer = csv.writer(new_csv)
#
#     for i in reader:
#         print(i)

# results = call("resolution=Fixed", 'search')
# # print(results)
# print(results['total'])

# response = call('project/18904?expand=details', 'get')
#
# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))

#url = 'https://cruise.okta.com/api/v1/groups?q=app-confluence-admin'
#
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': okta_token
# }
#
# response = requests.get(url, headers=headers)
#
# print(json.loads(response.text))

# name = 'app-confluence-admin'
# call = Okta.okta_groups(name)
# print(json.dumps(call, sort_keys=True, indent=4, separators=(",", ": ")))
# # for i in call:
# #     print(i['profile'])

# members = conf_call('group/system-administrators/member')
#
# for i in members['results']:
#     print(i['username'])
# results = field_metrics()
#
# print(json.dumps(results, sort_keys=True, indent=4, separators=(",", ": ")))

# define a list of strings
# strings_list = ["815 Last: 22/Mar/23 9:01 AM", "90 Last: 22/Mar/23 10:35 AM", "72331 Last: 22/Mar/23 12:16 PM"]
#
# # loop through each string in the list
# for i in range(len(strings_list)):
#     # find the index of "Last:" in the string
#     apple = strings_list[i]
#     last_index = strings_list[i].index("Last:")
#     # extract the date part of the string after "Last:"
#     print(last_index)
#     date_string = strings_list[i][last_index + len("Last:"):].strip()
#     # update the string in the list to only contain the date part
#     strings_list[i] = date_string
#
# # print the updated list of strings
# print(strings_list)

query = 'michelle.richards'

response = call("user?expand=groups", 'groups', query)


for i in response['groups']['items']:
    if "-agent" in i['name']:
        print(i['name'])

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))