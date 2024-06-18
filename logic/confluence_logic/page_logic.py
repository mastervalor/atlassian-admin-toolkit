from calls.confluence import Confluence


class Pages:

    def __init__(self):
        self.conf = Confluence()

    def create_page(self, space_key, title, content, ancestors):
        page_type = 'page'
        result = self.conf.create_content(page_type, space_key, title, content, ancestors)

        return result

    def generate_table_header(self, headers):
        # Create the table header based on the list of column names
        table_header = "<table>\n  <thead>\n    <tr>\n"
        for header in headers:
            table_header += f"      <th>{header}</th>\n"
        table_header += "    </tr>\n  </thead>\n  <tbody>\n"
        return table_header

    def find_content_in_page(self, page_id):
        page = self.conf.get_page(page_id)