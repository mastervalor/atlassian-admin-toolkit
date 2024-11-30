from logic.os_logic.json_logic import JSONLogic

json_logic = JSONLogic(open_file='automation-rules')
data = json_logic.json_file_manip.read_file()

if data:
    search_term = 'customfield_'

    total_occurrences = json_logic.count_occurrences(data, search_term)

    print(f"Total occurrences of '{search_term}' in 'automation-rules.json': {total_occurrences}")
else:
    print("Failed to read data from 'automation-rules.json'")


