from call import Jira

jira = Jira()

members = jira.remove_group_member("jira-new-hires", "aaron.cherian")

print(members)

# print(members, sort_keys=True, indent=4, separators=(",", ": "))