import unittest
from Bank_Account import BankAccount


class Test_Bank_Account(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Ivo", 10000, "$")

    def test_init(self):
        self.assertEqual(self.my_account.name, "Ivo")
        self.assertEqual(self.my_account.balance, 10000)
        self.assertEqual(self.my_account.currency, "$")

    def test_str(self):
        result = "Bank account for Ivo with balance of 10000$"
        self.assertEqual(str(self.my_account), result)

    def test_deposit(self):
        self.my_account.deposit(200)
        self.assertEqual(self.my_account.balance, 10200)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)
        self.assertEqual(self.my_account.balance, 10200)

    def test_transfer_different_currency(self):
        your_acc = BankAccount("Rado", 100, "&")
        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_acc, 200)
        self.assertEqual(self.my_account.balance, 10000)
        self.assertEqual(your_acc.balance, 100)


if __name__ == '__main__':
    unittest.main()
