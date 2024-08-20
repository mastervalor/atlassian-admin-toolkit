import unittest
from calls.okta import Okta
from dataformating.json_formating import JSONFormating

formating = JSONFormating()


class TestOktaUserApi(unittest.TestCase):

    def test_okta_user_api_get_user_profile(self):
        result = Okta.users_profile('mourad.marzouk@getcruise.com')
        formating.pretty_json(result)
