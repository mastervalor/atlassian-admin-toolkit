from logic.confluence_logic.space_logic import Spaces
from logic.os_logic.os_logic import OSLogic

# get pages Ids from a list of names
spaces = Spaces(is_staging=True)
os_logic = OSLogic(open_file='LucidChart', write_file='lucid chart page ids', columns=['Page ID'])
lucid_chart = os_logic.read_file()
spaces_list = []
page_ids = []

for space in lucid_chart:
    spaces_list.append(space['Space Name'])

space_ids = spaces.get_space_ids(spaces_list)
# get all restricted pages in a space and their IDs
for space_id in space_ids.values():
    restricted_pages = spaces.get_restricted_pages_in_space(space_id)
    page_ids.extend(restricted_pages)  # Add these pages to the main page_ids list

    # Print progress to track the process
    print(f"Space: {space_id} had restricted pages: {len(restricted_pages)}")

data_rows = [{'Page ID': page_id} for page_id in page_ids]
os_logic.write_to_file(data_rows)
