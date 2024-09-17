from calls.jira_api_calls.jira_api_user_calls import UserJiraCalls

user_api = UserJiraCalls()

print(user_api.get_user_by_key('JIRAUSER73627'))
