import json
import requests


class APIResponseHandler:
    def __init__(self, response):
        self.json_data = self._parse_response()
        self.response = response

    def _parse_response(self):
        try:
            return self.response.json()
        except ValueError:
            return {"error": "Invalid JSON response"}