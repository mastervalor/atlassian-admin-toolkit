from logic.os_logic.os_logic import OSLogic
from logic.jira_logic.project_logic import Projects

FINAL_LIST_OF_PROJECTS = []
project = Projects()


def add_to_the_list(file):
    for i in file:
        try:
            row = i['Project Key or Project Link (I.E. "CORPENG" for Corporate Engineering Project)']
        except KeyError:
            row = i['What is the Key of Your project?']

        if ',' in row:
            projects = row.split(', ')
            for project in projects:
                if project not in FINAL_LIST_OF_PROJECTS:
                    FINAL_LIST_OF_PROJECTS.append(project)
        else:
            FINAL_LIST_OF_PROJECTS.append(row)


jsm = OSLogic(open_file='JSM')
extras = OSLogic(open_file='extras')
software = OSLogic(open_file='Software standardization')

jsm_file = jsm.read_file()
extra_file = extras.read_file()
software_file = software.read_file()

add_to_the_list(extra_file)
add_to_the_list(software_file)
add_to_the_list(jsm_file)

print(FINAL_LIST_OF_PROJECTS)
