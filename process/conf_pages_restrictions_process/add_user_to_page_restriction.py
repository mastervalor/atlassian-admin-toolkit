from logic.confluence_logic.space_logic import Spaces
from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls
from calls.confluence_api_calls.conf_api_pages import ConfluencePageCalls
from logic.os_logic.os_logic import OSLogic
from dataformating.json_formating import JSONFormating

os_logic = OSLogic(open_file='LucidChart', write_file='lucid chart page ids', columns=['Page ID'])
spaces = Spaces(is_staging=True)
conf_spaces = ConfluenceSpaceCalls(is_staging=True)
conf_pages = ConfluencePageCalls(is_staging=True)

page_id = '64794020'
user_id = '557058:9ab63286-11ed-497d-8147-88b76e6c8a56'
my_id = '63c996ae6178fcc941d947ad'

# JSONFormating.pretty_json(conf_spaces.fetch_restrictions_for_page(Page_id))
self_response = conf_pages.add_user_to_page_restriction(page_id, 'update', my_id)
print(self_response.status_code)
print(self_response.text)

response = conf_pages.add_user_to_page_restriction(page_id, 'update', user_id)

print(response.status_code)
print(response.text)

