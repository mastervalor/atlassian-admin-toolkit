from calls.jira_api_calls.jira_api_workflow import WorkflowJiraCalls


class WorkflowLogic:
    def __init__(self,  is_staging=False):
        self.workflow_calls = WorkflowJiraCalls(is_staging=True) if is_staging else WorkflowJiraCalls()

    def delete_workflow(self, workflow_id):
        response = self.workflow_calls.delete_workflow(workflow_id)
        return response

    def get_workflow_id(self, workflow_name):
        workflow = self.workflow_calls.get_workflow_by_name(workflow_name)
        return workflow['values'][0]['id']['entityId']
