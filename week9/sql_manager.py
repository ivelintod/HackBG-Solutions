import sqlite3
from Client import Client
from settings import db_name
import re
import hashlib
import uuid


class ManageAccounts:

    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def change_message(self, new_message, logged_user):
        update_sql = '''UPDATE clients SET message = ?
            WHERE id = ?'''

        self.cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_email(self, new_email, logged_user):
        update_sql = '''UPDATE clients SET email = ?
            WHERE id = ?'''

        self.cursor.execute(update_sql, (new_email, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_email(new_email)

    def change_pass(self, new_pass, logged_user):
        update_sql = '''UPDATE clients SET password = ?
            WHERE id = ?'''

        self.cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        self.conn.commit()

    def reset_pass(self, new_pass, id):
        update_sql = '''UPDATE clients SET password = ?
            WHERE id = ?'''

        self.cursor.execute(update_sql, (new_pass, id))
        self.conn.commit()

    def register(self, username, password):
        insert_sql = '''INSERT INTO clients(username, password)
            VALUES (?, ?)'''

        self.cursor.execute(insert_sql, (username, password))
        self.conn.commit()

    def update_balance(self, money, logged_user):
        update_query = '''UPDATE clients SET balance = ?
            WHERE id = ?'''

        self.cursor.execute(update_query, (money, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_balance(money)

    def login(self, username):
        select_query = '''SELECT id, username, balance, message, password, email FROM clients
            WHERE username = ?'''

        self.cursor.execute(select_query, (username,))
        for user in self.cursor:
            if(user):
                return Client(user['id'], user['username'], user['balance'], user['message'], user['email'])
            else:
                return False

    def select_password(self, username):
        select_query = '''SELECT password FROM clients WHERE username = ?'''

        self.cursor.execute(select_query, (username, ))
        for row in self.cursor:
            return row['password']

    def select_email(self, name):
        select_query = '''SELECT email FROM clients WHERE username = ?'''

        self.cursor.execute(select_query, (name, ))
        for row in self.cursor:
            return row['email']

    def select_last_user(self):
        select_query = '''SELECT id FROM clients'''

        self.cursor.execute(select_query)
        cursor_duplicate = []
        for row in self.cursor:
            cursor_duplicate.append(row['id'])
        if len(cursor_duplicate) > 0:
            return cursor_duplicate[len(cursor_duplicate) - 1]

    def select_user_id(self, name):
        select_query = '''SELECT id FROM clients WHERE username = ?'''

        self.cursor.execute(select_query, (name,))
        selected_users = []
        for row in self.cursor:
            selected_users.append(row['id'])
        return selected_users[0]

    def list_user_names(self):
        select_query = '''SELECT username FROM clients'''

        self.cursor.execute(select_query)
        usernames = []
        for row in self.cursor:
            usernames.append(row['username'])
        return usernames

    def update_login_track_table(self, ids):
        insert_query = '''INSERT INTO  login_track(client_id) VALUES (?) '''

        self.cursor.execute(insert_query, (ids,))
        self.conn.commit()

    def select_user_logins(self, id):
        select_query = '''SELECT e1.login_attempt, e1.time FROM login_track AS e1, clients as e2
                          WHERE e1.client_id = ? LIMIT 1'''

        self.cursor.execute(select_query, (id,))
        login_attempts = []
        for row in self.cursor:
            login_attempts.append((row['login_attempt'], row['time']))
        return login_attempts[0]


    def failed_login_attempts(self, login_attempts, name):
        update_query = '''UPDATE login_track SET login_attempt = ? WHERE client_id = ?'''

        user_id = self.select_user_id(name)
        self.cursor.execute(update_query, (login_attempts, user_id))
        self.conn.commit()

    def time_of_block(self, time, name):
        update_query = '''UPDATE login_track SET time = ? WHERE client_id = ?'''

        user_id = self.select_user_id(name)
        self.cursor.execute(update_query, (time, user_id))
        self.conn.commit()


s = ManageAccounts()
#print(s.select_last_user())
