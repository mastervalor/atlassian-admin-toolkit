from logic.confluence_logic.space_logic import Spaces
from logic.os_logic.csv_logic import CSVLogic

# get pages Ids from a list of names
spaces = Spaces()
csv_logic = CSVLogic(open_file='LucidChart', write_file='lucid chart page ids', columns=['Page ID'])
lucid_chart = csv_logic.read_file()
spaces_list = []
page_ids = []

for space in lucid_chart:
    spaces_list.append(space['Space Name'])

space_ids = spaces.get_space_ids(spaces_list)
# get all restricted pages in a space and their IDs
for key,value in space_ids.items():
    restricted_pages = spaces.get_restricted_pages_in_space(value)
    page_ids.extend(restricted_pages)  # Add these pages to the main page_ids list

    # Print progress to track the process
    print(f"Space: {key}, ID: {value} had restricted pages: {len(restricted_pages)}")

data_rows = [{'Page ID': page_id} for page_id in page_ids]
csv_logic.write_to_file(data_rows)
