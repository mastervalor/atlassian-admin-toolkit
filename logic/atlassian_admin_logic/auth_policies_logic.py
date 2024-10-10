from calls.atlassian_admin_api_calls.auth_policies_api import AtlassianAuthPolicies
from dataformating.response_handling import APIResponseHandler
import math


class AuthPolicies:
    def __init__(self):
        self.auth_policies = AtlassianAuthPolicies()

    def get_status_of_task(self, task_id):
        response = self.auth_policies.get_task_status(task_id)

        # Use the APIResponseHandler to process the response
        handler = APIResponseHandler(response)

        # Check if the response was successful (2xx status code)
        if handler.get_status_code() == 200:
            task_status = handler.get_data()
            print("Task in progress:", task_status.get('inProgressCount', 0))
            print("Task success count:", task_status.get('successCount', 0))
            print("Task failure count:", task_status.get('failureCount', 0))
            return task_status

        # Handle any errors and print the appropriate message
        else:
            print(f"Error occurred: {handler.get_error_message()}")
            return {"error": handler.get_error_message(), "details": handler.get_data()}

    def add_users_to_auth_policies(self, users, policy_id):
        # Define chunk size (500 users per request)
        chunk_size = 500
        total_users = len(users)

        # Calculate how many batches are needed
        num_batches = math.ceil(total_users / chunk_size)

        for batch_num in range(num_batches):
            # Get the current batch of users (500 or less)
            start_index = batch_num * chunk_size
            end_index = min(start_index + chunk_size, total_users)
            user_batch = users[start_index:end_index]

            # Add the batch of users to the policy
            response = self.auth_policies.add_users_to_policy(user_batch, policy_id)

            # Check if there's a task ID to get the task status
            if 'taskId' in response:
                self.get_status_of_task(response['taskId'])
                print(f"Successfully moved batch {batch_num + 1} of users to policy {policy_id} with task id: "
                      f"{response['taskId']}")
            else:
                print(f"Error moving batch {batch_num + 1}: {response}")

        return f"All {total_users} users processed in {num_batches} batches."
