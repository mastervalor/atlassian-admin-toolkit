from logic.os_logic.json_logic import JSONLogic
from file_manip.csv_file_manip import CSVLogic

json_logic = JSONLogic(open_file='Modified_updated_rules copy', write_file='Modified_updated_rules updated')
csv_files = CSVLogic(open_file='Classic-CustomField')
data = json_logic.json_file_manip.read_file()
fields_file = csv_files.read_file()

# Ensure data was loaded successfully
if data is None or not fields_file:
    print("Failed to load JSON or CSV file.")
    exit()

# Preprocess the CSV data into a dictionary for faster lookups
fields_mapping = {row['serverId']: row['cloudId'] for row in fields_file}

# Define a search pattern for custom fields
search_pattern = r'customfield_\d+'

# Replace custom fields in the JSON data
updated_data = json_logic.replace_values(data, fields_mapping, search_pattern)

# Print the updated JSON data
print("Updated JSON Data:")
print(updated_data)

# Optionally, write the updated data back to the JSON file
json_logic.json_file_manip.write_file(updated_data)
