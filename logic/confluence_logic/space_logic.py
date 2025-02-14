import json
from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls
from calls.confluence_api_calls.conf_api_pages import ConfluencePageCalls

from urllib.parse import urlparse, parse_qs


class Spaces:
    def __init__(self, is_staging=False):
        self.conf_spaces = ConfluenceSpaceCalls(is_staging=True) if is_staging else ConfluenceSpaceCalls()
        self.conf_pages = ConfluencePageCalls(is_staging=True) if is_staging else ConfluencePageCalls()

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
                cursor = parse_qs(parsed_url.query).get('cursor', [None])[0]
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

    def get_pages_in_space(self, space_id):
        all_pages = []
        cursor = None

        while True:
            response_data = self.conf_spaces.fetch_pages_in_space(space_id, cursor)

            if not response_data:
                break

            all_pages.extend(response_data.get('results', []))

            if "_links" in response_data and "next" in response_data["_links"]:
                next_url = response_data["_links"]["next"]
                parsed_url = urlparse(next_url)
                cursor = parse_qs(parsed_url.query).get('cursor', [None])[0]
            else:
                break

        return all_pages

    def get_page_ids_in_space(self, space_id):
        page_ids = []
        cursor = None

        while True:
            # Fetch pages for the space with pagination support
            response_data = self.conf_spaces.fetch_pages_in_space(space_id, cursor)

            if not response_data:
                break

            # Collect the page IDs
            page_ids.extend([page['id'] for page in response_data.get('results', [])])

            # Check if there's more data to paginate through
            if "_links" in response_data and "next" in response_data["_links"]:
                next_url = response_data["_links"]["next"]
                parsed_url = urlparse(next_url)
                cursor = parse_qs(parsed_url.query).get('cursor', [None])[0]
            else:
                break

        return page_ids

    def get_restricted_pages_in_space(self, space_id):
        restricted_pages = []

        # Get all pages in the space
        all_pages = self.get_page_ids_in_space(space_id)

        # Check for restrictions on each page
        for page_id in all_pages:
            restrictions = self.conf_pages.fetch_restrictions_for_page(page_id)

            if not restrictions:
                continue

            # Check for any restrictions in the 'read' and 'update' operations
            read_restrictions = restrictions.get('read', {}).get('restrictions', {})
            update_restrictions = restrictions.get('update', {}).get('restrictions', {})

            # Check if there are any user or group restrictions in either 'read' or 'update'
            if read_restrictions.get('user', {}).get('results') or read_restrictions.get('group', {}).get('results') or \
                    update_restrictions.get('user', {}).get('results') or update_restrictions.get('group', {}).get(
                'results'):
                restricted_pages.append(page_id)

        return restricted_pages

    def set_space_permissions_by_groups_roles(self, key, group, role, target):
        payload = json.dumps({
            "subject": {
                "type": "group",
                "identifier": group
            },
            "operations": {
                "key": role,
                "target": target
            },
            "_links": {}
        })

        response = self.conf_spaces.set_space_permissions(key, payload)

        if response['statusCode'] == 400:
            print(f"Group: {group} in space: {key} with role {role, target}: {response}")

        return response

    def get_space_permissions(self, key):
        response = self.conf_spaces.get_space_permissions(key)
        return response

    def get_space_groups_by_roles(self, key, role):
        groups = self.conf_spaces.get_space_groups(key, role)
        return groups
