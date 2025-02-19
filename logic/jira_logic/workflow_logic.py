from calls.jira_api_calls.jira_api_workflow import WorkflowJiraCalls


class WorkflowLogic:
    def __init__(self,  is_staging=False):
        self.workflow_calls = WorkflowJiraCalls(is_staging=True) if is_staging else WorkflowJiraCalls()

    def delete_unused_workflow(self, name):


    def get_workflow_id(self, workflow_name):
        workflow = self.workflow_calls.get_workflow_by_name(workflow_name)
        return workflow['values'][0]['id']['entityId']