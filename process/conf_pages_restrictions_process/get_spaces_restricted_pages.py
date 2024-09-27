from logic.confluence_logic.space_logic import Spaces
from logic.confluence_logic.page_logic import Pages
from logic.os_logic.os_logic import OSLogic

# get pages Ids from a list of names
spaces = Spaces(is_staging=True)
pages = Pages(is_staging=True)
# os_logic = OSLogic(open_file='LucidChart')
# lucid_chart = os_logic.read_file()
# spaces_list = []

# for space in lucid_chart:
#     spaces_list.append(space['Space Name'])

# print(spaces_list)
# print(spaces.get_space_ids(spaces_list))
# get all restricted pages in a space and their IDs
# print(spaces_class.get_space_ids(['Information Technology']))

# Get all pages in a space
# pages = spaces.get_pages_in_space('64782345')
# print(f"Total pages in space: {len(pages)}")

# Get restricted pages in a space
page = ['64794020']
# restricted_pages = spaces.get_restricted_pages_in_space('64782345')
# print(f"Total restricted pages in space: {len(restricted_pages)}")
user_id = '557058:9ab63286-11ed-497d-8147-88b76e6c8a56'
spaces.add_user_edit_to_pages_restriction(page, user_id)
