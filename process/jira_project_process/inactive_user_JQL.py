import json
import concurrent.futures
import time
from logic.jira_logic.project_logic import Projects

project_logic = Projects()

active_projects = project_logic.get_active_all_project_keys()

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(project_logic.reassign_inactive_users, active_projects)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')
