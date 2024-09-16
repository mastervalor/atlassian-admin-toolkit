from logic.os_logic.os_logic import OSLogic

FINAL_LIST_OF_PROJECTS = []

jsm = OSLogic(open_file='JSM')
extras = OSLogic(open_file='extras')
software = OSLogic(open_file='Software standardization')

jsm_file = jsm.read_file()
extra_file = extras.read_file()
software_file = software.read_file()

final_lis_of_projects = []

for i in extra_file:
    row = i['Project Key or Project Link (I.E. "CORPENG" for Corporate Engineering Project)']
    if ',' in row:
        projects = row.split(', ')
        for project in projects:
            if project not in final_lis_of_projects:
                final_lis_of_projects.append(project)
    else:
        final_lis_of_projects.append(row)


print(final_lis_of_projects)
