from logic.jira_logic.field_logic import Fields
from dataformating.json_formating import JSONFormating

fields = Fields()
formating = JSONFormating()


def test_field_options(field_id, context_id):
    field_options = fields.field_options(field_id, context_id)
    if field_options.status_code == 200:
        print("Successfully mad call")
        formating.pretty_json(field_options)
    else:
        print(field_options.status_code, field_options.text)
