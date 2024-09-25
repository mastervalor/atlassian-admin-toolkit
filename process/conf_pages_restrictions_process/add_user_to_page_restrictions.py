from logic.confluence_logic.space_logic import Spaces

# get pages Ids from a list of names
spaces = Spaces(is_staging=True)
spaces_list =[]
spaces.get_space_ids(spaces_list)
# get all restricted pages in a space and their IDs
# add user to all those restricted pages with edit

