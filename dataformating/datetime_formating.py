from datetime import datetime


class DateTimeFormating:
    @staticmethod
    def format_datetime(iso_string):
        """
        Converts an ISO 8601 date string to a human-readable format.
        :param iso_string: The ISO 8601 date string to format.
        :return: A formatted date string or 'None' if the input is invalid.
        """
        if iso_string:
            try:
                dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))  # Handle ISO strings
                return dt.strftime("%B %d, %Y, %I:%M %p UTC")
            except ValueError:
                return iso_string  # Return as-is if there's an issue
        return "None"

