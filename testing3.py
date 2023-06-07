from call import Confluence
import json


instance = Confluence()
page_tree = instance.get_child_pages_recursive('465649108')
print(json.dumps(page_tree, sort_keys=True, indent=4, separators=(",", ": ")))
