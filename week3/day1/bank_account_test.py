import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.currency = "BGN"
        self.account = BankAccount("Ivo", 0, self.currency)
        self.account2 = BankAccount("Rado", 1000, self.currency)

    def test_can_create_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_invalid_initial_balance(self):
        with self.assertRaises(ValueError):
            test_ac = BankAccount("Person", -50, self.currency)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(500, self.account.balance)
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_current_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)
            self.account.withdraw(-100)

    def test_transfer_to(self):
        self.account2.transfer_to(self.account, 100)
        self.assertEqual(self.account.balance, 100)
        self.assertEqual(self.account2.balance, 900)
        with self.assertRaises(ValueError):
            self.account.transfer_to(self.account2, 120)
            self.account.transfer_to(self.account2, -50)

    def test_history(self):
        self.account2.transfer_to(self.account, 200)
        expected = ['Transfer to Ivo for 200BGN']
        self.assertEqual(self.account2.account_history(),expected)




if __name__ == '__main__':
    unittest.main()
