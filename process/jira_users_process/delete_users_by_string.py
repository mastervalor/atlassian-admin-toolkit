from logic.jira_logic.user_logic import Users
from calls.jira import Jira
import json

# user = Users(is_staging=True)
#
# user.get_usernames_by_search_string('')

jira = Jira(is_staging=True)

user = jira.find_users_by_string('mourad.marzouk', 50, 0)

print(user[0]['emailAddress'])
