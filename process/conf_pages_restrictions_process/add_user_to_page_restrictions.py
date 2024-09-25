from logic.confluence_logic.space_logic import Spaces
from logic.os_logic.os_logic import OSLogic

# get pages Ids from a list of names
spaces = Spaces(is_staging=True)
os_logic = OSLogic(open_file='LucidChart')
lucid_chart = os_logic.read_file()
spaces_list = []

for space in lucid_chart:
    spaces_list.append(space['Space Name'])

print(spaces_list)
print(spaces.get_space_ids(spaces_list))
# get all restricted pages in a space and their IDs

# add user to all those restricted pages with edit
