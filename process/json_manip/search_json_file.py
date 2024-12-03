from logic.os_logic.json_logic import JSONLogic
from file_manip.csv_file_manip import CSVLogic

json_logic = JSONLogic(open_file='automation-rules')
csv_files = CSVLogic(open_file='Classic-CustomField')
data = json_logic.json_file_manip.read_file()
fields_file = csv_files.read_file()

if data:
    search_term = 'customfield_'

    total_occurrences = json_logic.count_occurrences(data, search_term)

    print(f"Total occurrences of '{search_term}' in 'automation-rules.json': {total_occurrences}")
else:
    print("Failed to read data from 'automation-rules.json'")

if data:
    search_pattern = r'customfield_\d+'

    matches = json_logic.find_occurrences(data, search_pattern)

    unique_matches = set(matches)

    print(f"Found the following custom fields in 'automation-rules.json':")
    for match in unique_matches:
        field_id = match.split('customfield_')[1]
        print(field_id)
else:
    print("Failed to read data from 'automation-rules.json'")


