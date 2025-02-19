#!/usr/bin/python
import json
import re
import subprocess

import requests

from auth import auth

cmd = 'acli --action renderRequest --request /secure/admin/workflows/ListWorkflows.jspa'

response = subprocess.check_output(cmd.split()).decode("utf-8")

count = 0


for line in response.splitlines():
    str = "NTBD"
    matchdelete = re.search('<a data-operation="delete" class="trigger-dialog" id="del_(.*)" href="DeleteWorkflow\.jspa', line)
    if matchdelete:
        if str not in matchdelete.group(1):
            name = matchdelete.group(1)

            url = "https://lucidmotors.atlassian.net/rest/api/3/workflow/search?workflowName=" + name

            auth = auth
            headers = {

                "Accept": "application/json"

            }
            workflow = requests.request(
                "GET",
                url,
                headers=headers,
                auth=auth
            ).text

            workflow = json.loads(workflow)

            id = workflow['values'][0]['id']['entityId']

            url = "https://lucidmotors.atlassian.net/rest/api/3/workflow/" + id

            auth = auth

            response = requests.request(
                "DELETE",
                url,
                auth=auth
            )

            print(response.text)

        count += 1

