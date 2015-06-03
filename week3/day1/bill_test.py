import unittest
from bill import Bill

class BillTest(unittest.TestCase):

    def setUp(self):
        self.my_bill = Bill(5)

    def test_create_new_bill_instance(self):
        self.my_bill.amount = 15
        self.assertTrue(isinstance(self.my_bill, Bill))

    def test_valid_amount(self):
        self.assertEqual(self.my_bill.amount, 5)

    def test_int_cast(self):
        self.assertTrue(int(self.my_bill, 5))

    def test_str_cast(self):
        self.assertEqual(str(self.my_bill, "5"))

    def test_eq(self):
        my_other_bill = Bill(5)
        self.assertTrue(self.my_bill == my_other_bill)

if __name__ == '__main__':
    unittest.main()
