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
        rows = table.find_all('tr')
        table_data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols:
                table_data.append(cols)
        return table_data, soup, table

    def update_table_row(self, table, project_key_to_find, new_approver):
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols and len(cols) > 1:
                project_key = cols[1].text.strip()
                if project_key == project_key_to_find:
                    approver = cols[2].text.strip()
                    if approver != new_approver:
                        cols[2].string.replace_with(new_approver)
                        return True
        return False

    def update_approver_in_page(self, page_id, project_key_to_find, new_approver):
        # Get the page content
        page_data = self.conf.get_page(page_id)

        if not page_data:
            return

        # Extract page content and version
        page_content = page_data['body']['storage']['value']
        version = page_data['version']['number']
        title = page_data['title']
        page_type = 'page'

        # Parse the table
        table, soup = self.parse_table(page_content)

        # Update the table row if necessary
        if table:
            updated = self.update_table_row(table, project_key_to_find, new_approver)
            if updated:
                updated_page_content = str(soup)
                self.conf.update_content(page_id, page_type, title, updated_page_content, version)
            else:
                print("No update needed; approver already correct.")
        else:
            print("Table not found in the page content.")

    def clear_page_content(self, page_id):
        page_data = self.conf.get_page(page_id)
        if not page_data:
            return False

        current_version = page_data['version']['number']
        page_title = page_data['title']
        page_type = page_data['type']

        if self.conf.update_content(page_id, page_type, page_title, "", current_version):
            print(f"Content of page '{page_id}' cleared successfully!")
            return True
        else:
            print(f"Failed to clear content of page '{page_id}'.")
            return False
