import unittest
from panda import Panda


class Test_Panda(unittest.TestCase):

    def setUp(self):
        self.my_account = Panda("Ivo", "ivo_b@mail.bg", "male")
        self.your_account = Panda("Vlado", "vlado@abv.bg", "female")

    def test_init(self):
        self.assertEqual(self.my_account._name, "Ivo")
        self.assertEqual(self.my_account._email, "ivo_b@mail.bg")
        self.assertEqual(self.my_account._gender, "male")


    def test_str(self):
        result = "Panda's name, email and gender are Ivo, ivo_b@mail.bg, male"
        self.assertEqual(str(self.my_account), result)

    def test_equal(self):
        self.assertTrue(self.my_account.__eq__)

    def test_isMale(self):
        self.assertEqual(self.my_account._gender, "male")

    def test_isFemale(self):
        self.assertEqual(self.your_account._gender, "female")

    def test_email(self):
        with self.assertRaises(ValueError):
            self.my_account.set_email("1234")

    def test_hash(self):
        result = self.my_account.__hash__()
        self.assertTrue(isinstance(result, int))

class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.my_account = ivo.Panda

    def test_add_panda(self):
        with self.assertRaises(Exception):
            self.assertTrue()


if __name__ == "__main__":
    unittest.main()

