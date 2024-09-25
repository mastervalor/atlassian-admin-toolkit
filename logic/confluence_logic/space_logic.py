from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls


class Spaces:
    def __init__(self, is_staging=False):
        self.conf_spaces = ConfluenceSpaceCalls(is_staging=True) if is_staging else ConfluenceSpaceCalls()

    def get_all_spaces(self):
        all_spaces = self.conf_spaces.get_spaces()['results']

    def get_space_ids(self, spaces_list):
        all_spaces = self.conf_spaces.get_spaces()['results']
        print(len(all_spaces))
        for spaces in all_spaces:
            print(spaces)
