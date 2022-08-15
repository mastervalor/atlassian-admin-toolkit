import requests
from requests.auth import HTTPBasicAuth
import json

IN_DEVELOPMENT = False

if IN_DEVELOPMENT:
   JIRA_BASE_URL = 'https://lucidmotors-sandbox-693.atlassian.net/rest/api/3/workflow/'
else:
   JIRA_BASE_URL = 'https://lucidmotors.atlassian.net/rest/api/3/workflow/'

JIRA_SEARCH_WF_NAME = 'search?workflowName='
WORKFLOW_NAME = 'BE: SR workflow'
JIRA_GET_WORKFLOW = JIRA_BASE_URL + JIRA_SEARCH_WF_NAME + WORKFLOW_NAME

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

headers = {"Accept": "application/json"}

id = json.loads(requests.get(JIRA_GET_WORKFLOW, auth=auth, headers=headers).text)['values'][0]['id']['entityId']

print(id)
