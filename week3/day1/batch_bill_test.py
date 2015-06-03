from batch_bill import BatchBill
from bill import Bill
import unittest

class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.values = [10, 20, 50, 100]
        self.bills = [Bill(value) for value in self.values]
        self.my_batch = BatchBill(self.bills)
    def test_init(self):

        self.assertTrue(isinstance(self.my_batch, BatchBill))
        self.assertEqual(self.my_batch.bills, self.bills)

    def test_iteration(self):
        self.assertEqual(self.my_batch[1] == self.bills[1])

if __name__ == '__main__':
    unittest.main()
