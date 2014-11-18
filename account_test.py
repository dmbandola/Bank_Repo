import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def test_account_object_can_be_created(self):
        account = Account("001", 50)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50)

    def setUp(self):
        self.acc = Account("001", 50)

    def test_add_method_raises_typeerror_if_not_int(self):
        self.assertRaises(TypeError, self.acc.check_if_int, "001", "50")

if __name__ == '__main__':
    unittest.main()
