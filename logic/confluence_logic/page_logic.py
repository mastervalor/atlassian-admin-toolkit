from calls.confluence import Confluence
from bs4 import BeautifulSoup

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

    def generate_table_content(self, projects, headers):
        # Generate the table header
        table_content = self.generate_table_header(headers)

        # Loop through the project data and create table rows
        for project in projects:
            table_content += "    <tr>\n"
            for header in headers:
                table_content += f"      <td>{project.get(header.lower().replace(' ', '_'), '')}</td>\n"
            table_content += "    </tr>\n"

        # Close the table
        table_content += "  </tbody>\n</table>\n"

        return table_content

    def parse_table(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        table = soup.find('table')
        return table, soup