from logic.confluence_logic.space_logic import Spaces
from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls
from dataformating.json_formating import JSONFormating


from logic.os_logic.os_logic import OSLogic

# get pages Ids from a list of names
# spaces = Spaces(is_staging=True)
# os_logic = OSLogic(open_file='LucidChart')
# lucid_chart = os_logic.read_file()
# spaces_list = []
#
# for space in lucid_chart:
#     spaces_list.append(space['Space Name'])
#
# print(spaces_list)
# print(spaces.get_space_ids(spaces_list))
# get all restricted pages in a space and their IDs
spaces_class = Spaces(is_staging=True)
space_calls = ConfluenceSpaceCalls(is_staging=True)
# print(spaces_class.get_space_ids(['Information Technology']))

# Get all pages in a space
# pages = spaces_class.get_pages_in_space('96206863')
# print(f"Total pages in space: {len(pages)}")

# Get restricted pages in a space
restricted_pages = spaces_class.get_restricted_pages_in_space('96206863')
print(f"Total restricted pages in space: {len(restricted_pages)}")

# JSONFormating.pretty_json(space_calls.fetch_restrictions_for_page('96207758'))

# add user to all those restricted pages with edit
# 96207758