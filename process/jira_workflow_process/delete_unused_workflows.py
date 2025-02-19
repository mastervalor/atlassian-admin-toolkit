#!/usr/bin/python
import re
import subprocess
from logic.jira_logic.workflow_logic import WorkflowLogic


cmd = 'acli --action renderRequest --request /secure/admin/workflows/ListWorkflows.jspa'

response = subprocess.check_output(cmd.split()).decode("utf-8")
workflow_logic = WorkflowLogic()
count = 0
name_substring = "NTBD"


for line in response.splitlines():
    match_delete = re.search('<a data-operation="delete" class="trigger-dialog" id="del_(.*)" href="DeleteWorkflow\.jspa', line)
    if match_delete:
        if name_substring not in match_delete.group(1):
            workflow_name = match_delete.group(1)
            
            workflow_id = workflow_logic.get_workflow_id(workflow_name)
            response = workflow_logic.delete_workflow(workflow_id)

        count += 1
