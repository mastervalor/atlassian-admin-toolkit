from logic.jira_logic.user_logic import Users

user = Users(is_staging=True)

user.get_usernames_by_search_string('es.cloudfactory.com')