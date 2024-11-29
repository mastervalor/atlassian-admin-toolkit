from logic.os_logic.json_logic import JSONLogic

json_logic = JSONLogic(open_file='automation-rules')
json_file = json_logic.read_file()

for i in json_file:
    print(i)
    