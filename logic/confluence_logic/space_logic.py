from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls
from urllib.parse import urlparse, parse_qs


class Spaces:
    def __init__(self, is_staging=False):
        self.conf_spaces = ConfluenceSpaceCalls(is_staging=True) if is_staging else ConfluenceSpaceCalls()

    def get_all_spaces(self):
        all_spaces = []
        cursor = None
        while True:
            # Fetch a single page of spaces
            response_data = self.conf_spaces.get_spaces(cursor=cursor)

            if not response_data:
                break

            all_spaces.extend(response_data.get('results', []))

            if "_links" in response_data and "next" in response_data["_links"]:
                next_url = response_data["_links"]["next"]
                parsed_url = urlparse(next_url)
                cursor = parse_qs(parsed_url.query).get('cursor', [None])[0]  # Update cursor for the next batch
            else:
                break

        return all_spaces

    def get_space_ids(self, spaces_list):
        spaces_with_ids = {}
        all_spaces = self.get_all_spaces()
        for spaces in all_spaces:
            if spaces['name'] in spaces_list:
                spaces_with_ids[spaces['name']] = spaces['id']

        return spaces_with_ids
