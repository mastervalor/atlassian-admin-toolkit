import json
import requests


class APIResponseHandler:
    def __init__(self, response):
        self.parsed_data = self._parse_response()
        self.status_code = response.status_code
        self.response = response

    def _parse_response(self):
        try:
            return self.response.json()
        except ValueError:
            return {"error": "Invalid JSON response",  "text": self.response.text}

    def handle_response(self):
        # Check for known status codes and return useful information
        if self.status_code == 200:
            return self._handle_success()
        elif self.status_code == 400:
            return self._handle_client_error()
        elif self.status_code == 401:
            return {"error": "Unauthorized. Please check your credentials."}
        elif self.status_code == 403:
            return {"error": "Forbidden. You don’t have permission to access this resource."}
        elif self.status_code == 404:
            return self._handle_not_found()
        elif self.status_code == 429:
            return {"error": "Too Many Requests. Rate limit exceeded."}
        elif self.status_code == 500:
            return {"error": "Internal Server Error. Try again later."}
        else:
            # Handle any other unexpected status codes
            return self._handle_unknown_status_code()

    def _handle_success(self):
        # Handles 200 OK responses
        message = self.parsed_data.get("message", "Request was successful.")
        return {"status": "success", "message": message, "data": self.parsed_data}

    def _handle_client_error(self):
        # Handles 400 Bad Request responses
        errors = self.parsed_data.get("errors", [])
        return {
            "status": "client_error",
            "message": "Bad Request.",
            "errors": errors or "No specific errors provided.",
        }

    def _handle_not_found(self):
        # Handles 404 Not Found responses
        errors = self.parsed_data.get("errors", [])
        return {
            "status": "not_found",
            "message": "Resource not found.",
            "errors": errors or "No specific details provided.",
        }

    def _handle_unknown_status_code(self):
        # Generic handler for unexpected status codes
        return {
            "status": "unknown_status",
            "status_code": self.status_code,
            "response": self.parsed_data or self.response.text,
        }

    def get_parsed_data(self):
        # Returns the raw parsed data from the response
        return self.parsed_data
    