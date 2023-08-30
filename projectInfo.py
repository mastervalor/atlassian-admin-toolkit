import json
import os
import csv
import getpass
from call import Jira

jira = Jira()

response = jira.get_project('REQFN')


# "projectTypeKey"

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))