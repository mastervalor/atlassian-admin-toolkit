from logic.os_logic.os_logic import OSLogic

FINAL_LIST_OF_PROJECTS = []


def add_to_the_list(file):
    for i in file:
        row = i['Project Key or Project Link (I.E. "CORPENG" for Corporate Engineering Project)']
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

print(FINAL_LIST_OF_PROJECTS)
