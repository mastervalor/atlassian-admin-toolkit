from calls.atlassian_admin_api_calls.auth_policies_api import AtlassianAuthPolicies
import math


class AuthPolicies:
    def __init__(self):
        self.auth_policies = AtlassianAuthPolicies()

    def get_status_of_task(self, task_id):
        response = self.auth_policies.get_task_status(task_id)

        # Check the status code of the response
        if response.status_code == 200:
            # Request succeeded, process the task status
            task_status = response.json()
            print("Task in progress:", task_status.get(' ', 0))
            print("Task success count:", task_status.get('successCount', 0))
            print("Task failure count:", task_status.get('failureCount', 0))
            return task_status

        elif response.status_code == 400:
            # Handle bad request
            print("Bad request. Please check the syntax or parameters.")
            return {"error": "Bad Request", "details": response.json()}

        elif response.status_code == 401:
            # Handle unauthorized access
            print("Unauthorized access. Please check your authentication token.")
            return {"error": "Unauthorized", "details": response.json()}

        elif response.status_code == 404:
            # Handle not found
            print(f"Task with ID {task_id} not found.")
            return {"error": "Not Found", "details": response.json()}

        elif response.status_code == 429:
            # Handle rate limiting
            print("Rate limit exceeded. Please try again later.")
            return {"error": "Too Many Requests", "details": response.json()}

        elif response.status_code == 500:
            # Handle internal server error
            print("Server error. Please try again later.")
            return {"error": "Internal Server Error", "details": response.json()}

        else:
            # Handle unexpected status codes
            print(f"Unexpected error: {response.status_code}")
            return {"error": f"Unexpected error {response.status_code}", "details": response.text}

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
