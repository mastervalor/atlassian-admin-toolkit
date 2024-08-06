from call import call, project_metric

response = call('project', 'get')
projects = {}

for i in response:
    projects[i['key']] = [i['name'], i['projectTypeKey'], i['id']]

for key in projects:
    project = project_metric(key)
    for l in project:
        projects[key].append(l)
    print(projects[key])
