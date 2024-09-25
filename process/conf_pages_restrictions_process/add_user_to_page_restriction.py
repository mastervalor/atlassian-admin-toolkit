from logic.confluence_logic.space_logic import Spaces
from calls.confluence_api_calls.conf_api_spaces import ConfluenceSpaceCalls
from dataformating.json_formating import JSONFormating


spaces = Spaces(is_staging=True)
conf_spaces = ConfluenceSpaceCalls(is_staging=True)

Page_id = '96207758'
user_id = '557058:9ab63286-11ed-497d-8147-88b76e6c8a56'

JSONFormating.pretty_json(conf_spaces.fetch_restrictions_for_page(Page_id))


