from calls.jira_api_calls.jira_api_workflow import WorkflowJiraCalls


class WorkflowLogic:
    def __init__(self,  is_staging=False):
        self.workflow_calls = WorkflowJiraCalls(is_staging=True) if is_staging else WorkflowJiraCalls()

        