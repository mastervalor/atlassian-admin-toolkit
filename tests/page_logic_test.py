from logic.confluence_logic.page_logic import Pages
from dataformating.json_formating import JSONFormating

page = Pages()
formating = JSONFormating()


def test_get_page_type(page_id):
    page_type = page.get_page_type(page_id)
    formating.pretty_json(page_type)


test_get_page_type('355776435')