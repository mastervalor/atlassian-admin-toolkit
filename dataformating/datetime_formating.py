from datetime import datetime
from zoneinfo import ZoneInfo


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
                dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))  # Convert ISO to datetime
                dt_utc = dt.astimezone(ZoneInfo("UTC"))  # Normalize to UTC
                pt_timezone = ZoneInfo("America/Los_Angeles")  # Pacific Time (PT) timezone
                dt_pt = dt_utc.astimezone(pt_timezone)  # Convert to Pacific Time
                return dt_pt.strftime("%B %d, %Y, %I:%M %p %Z")  # Include timezone in output
            except (ValueError, ZoneInfo.KeyError):
                return iso_string  # Return as-is if there's an issue
        return "None"

