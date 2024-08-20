import unittest
from logic.okta_logic.okta_user_logic import OktaUsers


class TestOktaUserLogic(unittest.TestCase):

    def test_okta_user_logic_get_user_manager(self):
        test_param = 'david.cooke'
        result = OktaUsers.get_user_manager('mourad.marzouk@getcruise.com')
        self.assertEqual(result, test_param)

    def test_okta_user_logic_get_user_status(self):
        test_param = 'ACTIVE'
        result = OktaUsers.get_user_status('mourad.marzouk@getcruise.com')  # Corrected method name
        self.assertEqual(result, test_param)

    def test_okta_user_logic_get_user_id(self):
        test_param = '00uq50f3fpe68fBOB1t7'
        result = OktaUsers.get_user_id('mourad.marzouk')
        self.assertEqual(result, test_param)


if __name__ == '__main__':
    unittest.main()
