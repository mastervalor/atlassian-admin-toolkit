import unittest
from calls.okta_api_calls.okta_users_api import OktaUsersCalls
from dataformating.json_formating import JSONFormating

formating = JSONFormating()


class TestOktaUserApi(unittest.TestCase):

    def test_okta_user_api_get_user_profile(self):
        result = OktaUsersCalls.users_profile('mourad.marzouk@getcruise.com')
        formating.pretty_json(result)
