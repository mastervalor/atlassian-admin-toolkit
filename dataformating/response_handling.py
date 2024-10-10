import json


class APIResponseHandler:
    def __init__(self, response):
        """
        Initialize the handler with the API response.
        """
        self.response = response
        self.status_code = response.status_code
        self.data = None
        self.error_message = None
        self.parse_response()

    def parse_response(self):
        """
        Parse the response based on the status code.
        This method will handle the different types of content returned by the API.
        """
        if 200 <= self.status_code < 300:
            self.handle_success()
        elif 300 <= self.status_code < 400:
            self.handle_redirection()
        elif 400 <= self.status_code < 500:
            self.handle_client_error()
        elif 500 <= self.status_code < 600:
            self.handle_server_error()
        else:
            self.error_message = f"Unhandled status code: {self.status_code}"

    def handle_success(self):
        """
        Handle 2xx success responses.
        Tries to parse the response data, if available.
        """
        try:
            if self.response.content:
                self.data = self.response.json()  # If it's JSON
            else:
                self.data = "No content in the response."
        except json.JSONDecodeError:
            self.data = self.response.text  # For non-JSON responses

    def handle_redirection(self):
        """
        Handle 3xx redirection responses.
        """
        self.error_message = f"Redirection occurred: {self.status_code}. Location: {self.response.headers.get('Location', 'Unknown')}"

    def handle_client_error(self):
        """
        Handle 4xx client error responses.
        """
        try:
            self.error_message = self.response.json().get("error", self.response.text)
        except json.JSONDecodeError:
            self.error_message = self.response.text

    def handle_server_error(self):
        """
        Handle 5xx server error responses.
        """
        try:
            self.error_message = self.response.json().get("error", self.response.text)
        except json.JSONDecodeError:
            self.error_message = self.response.text

    def get_status_code(self):
        return self.status_code

    def get_data(self):
        return self.data

    def get_error_message(self):
        return self.error_message
