from calls.confluence import Confluence


class Spaces:

    def __init__(self):
        self.conf = Confluence()

    def create_page(self, space_key, title, content, ancestors):
        page_type = 'page'
        result = self.conf.create_content(page_type, space_key, title, content, ancestors)

        return result
