from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls


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
                cursor = response_data["_links"]["next"]  # Update cursor for the next batch
            else:
                break

        return all_spaces

    def get_space_ids(self, spaces_list):
        spaces = {}
        all_spaces = self.get_all_spaces()
        for spaces in all_spaces:
            if spaces['name'] in spaces_list:
                spaces['name'] = spaces['id']

        return spaces
