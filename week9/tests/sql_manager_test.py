import sys
import unittest
import sqlite3
import os
from getpass import getpass
import create_tables_tests
from settings_for_tests import DB_NAME
sys.path.append("..")
from sql_manager import ManageAccounts


class SqlManagerTests(unittest.TestCase):
    password = getpass(prompt='Enter password for test: ')

    def setUp(self):
        create_tables_tests.main()
        self.manager = ManageAccounts()
        self.manager.conn = sqlite3.connect(DB_NAME)
        self.manager.conn.row_factory = sqlite3.Row
        self.manager.cursor = self.manager.conn.cursor()
        self.manager.register('Tester', '123AAAAA!')

    #def tearDown(self):
     #   self.manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        #os.remove("bank.db")
        os.remove("test_bank.db")

    def test_register_with_invalid_password(self):
        registration = self.manager.register('YourMum', '12YourMumzz@')
        self.assertFalse(registration)

    def test_register(self):
        self.manager.register('Dinko', '123123AZ%')

        self.manager.cursor.execute('''SELECT Count(*)  FROM clients
            WHERE username = (?)''', ('Dinko',))

        users_count = self.manager.cursor.fetchone()

        self.assertEqual(users_count['Count(*)'], 1)

    def test_login(self):
        logged_user = self.manager.login('Tester')
        self.assertEqual(logged_user.get_username(), 'Tester')

    '''def test_login_wrong_password(self):
        logged_user = self.manager.login('Tester')
        self.assertFalse(logged_user)'''

    def test_change_message(self):
        logged_user = self.manager.login('Tester')
        new_message = "podaivinototam"
        self.manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.manager.login('Tester')
        new_password = "12345zzzZ@"
        self.manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_change_invalid_password(self):
        logged_user = self.manager.login('Tester')

        new_password = ['123A@', '123AAAAAA', '1232432442', '@@@123', '1234aaaa@', 'aaaaaaaaa', '11213TesteraaAA@@112']
        for password in new_password:
            change_pass = self.manager.change_pass(password, logged_user)
            self.assertFalse(change_pass)

    def test_security(self):
        logged_user = self.manager.login('100 OR 1=1')
        self.assertFalse(logged_user)


class test_hidden_password_characters(SqlManagerTests):

    def test_pass(self):
            self.assertEqual(self.password, '1234A')

    def test_pass2(self):
            modified_pass = self.password[2:]
            self.assertEqual(modified_pass, '34A')

if __name__ == '__main__':
    unittest.main()
