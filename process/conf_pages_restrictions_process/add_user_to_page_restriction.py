from calls.confluence_api_calls.conf_api_pages import ConfluencePageCalls
from logic.os_logic.csv_logic import CSVLogic

csv_logic = CSVLogic(open_file='lucid chart page ids')
restricted_pages = csv_logic.read_file()
conf_pages = ConfluencePageCalls()


user_id = '557058:9ab63286-11ed-497d-8147-88b76e6c8a56'
my_id = '63c996ae6178fcc941d947ad'

for page_id in restricted_pages:
    self_response = conf_pages.add_user_to_page_restriction(page_id['Page ID'], 'update', my_id)
    print(f'page is: {page_id}: has come back with status code:  {self_response.status_code}')
    print(self_response.text)

    response = conf_pages.add_user_to_page_restriction(page_id['Page ID'], 'update', user_id)

    print(f'page is: {page_id}: has come back with status code:  {response.status_code}')
    print(response.text)

