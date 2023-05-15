from call import Confluence
import json


page_tree = Confluence.get_child_pages_recursive('324733855')
print(json.dumps(page_tree, sort_keys=True, indent=4, separators=(",", ": ")))
