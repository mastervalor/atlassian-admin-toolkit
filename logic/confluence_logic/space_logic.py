from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls


class Spaces:
    def __init__(self, is_staging=False):
        self.conf_spaces = ConfluenceSpaceCalls(is_staging=True) if is_staging else ConfluenceSpaceCalls()

    def get_project_ids(self, spaces_list):
        all_spaces = self.conf_spaces.get_spaces()

        for spaces in all_spaces['results']:
            print(spaces)
