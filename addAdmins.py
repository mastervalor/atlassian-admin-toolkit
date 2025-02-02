from logic.jira_logic.project_logic import Projects
import csv
import os
import requests
import json
from auth import auth, staging_auth

project_logic = Projects()
group = "administrators"
project_key = ''

print(project_logic.add_group_admins_to_project(group, project_key))
