from auth import auth
import json
import requests
from call import call, project_metric


# def call(ext):
#     url = f"https://jira.robot.car/rest/api/2/project/{ext}"
#
#     headers = {
#         "Accept": "application/json"
#     }
#
#     response = json.loads(requests.request(
#         "GET",
#         url,
#         headers=headers,
#         auth=auth
#     ).text)
#
#     return response
#
#
# def search(payload):
#     url = f"https://jira.robot.car/rest/api/2/search"
#
#     headers = {
#         "Accept": "application/json"
#     }
#
#     query = {
#         'jql': f'project = {payload} ORDER BY created DESC'
#     }
#
#     response = json.loads(requests.request(
#         "GET",
#         url,
#         headers=headers,
#         params=query,
#         auth=auth
#     ).text)
#
#     return response


response = call('project', 'get')
projects = {}

for i in response:
    projects[i['key']] = [i['name'], i['projectTypeKey'], i['id']]

for key in projects:
    project = project_metric(key)
    for l in project:
        projects[key].append(l)
    print(projects[key])
