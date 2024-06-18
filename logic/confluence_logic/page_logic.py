from calls.confluence import Confluence


class Pages:

    def __init__(self):
        self.conf = Confluence()

    def create_page(self, space_key, title, content, ancestors):
        page_type = 'page'
        result = self.conf.create_content(page_type, space_key, title, content, ancestors)

        return result

    def find_content_in_page(self, page_id, content):
        page = self.conf.get_page(page_id)