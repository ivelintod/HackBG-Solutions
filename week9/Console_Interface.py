from sql_manager import ManageAccounts
import hashlib
import uuid
import getpass
import time
import re
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


class Interface:

    def __init__(self):
        self.manager = ManageAccounts()
        self.start_commands = ['login', 'register', 'send-reset-password','reset-password', 'exit']
        self.login_commands = ['info', 'changepass', 'change-message', 'show-message', 'deposit', 'withdraw', 'help']
        self.user_is_suspended = False
        self.unique_random_code = uuid.uuid4().hex
        self.recipient = None
        self.TAN_codes = None

    def register_name_check(self):
        username = input('Enter your username: ')
        list_of_usernames = self.manager.list_user_names()
        if username in list_of_usernames:
            print('Username already taken!')
            self.register_name_check()

        if username == '':
            print('Invalid username!')
            return self.register_name_check()

        for i in '0123456789':
            if i in username:
                print('Invalid username!')
                return self.register_name_check()

        return username

    def register_password_security_check(self, name):
        password = input('Enter your password: ')

        if not self.password_security_check(password, name) or password == '':
            print('Invalid password!')
            return self.register_password_security_check(name)

        return password

    def register_process(self):
        username = self.register_name_check()
        password = self.register_password_security_check(username)
        hashed_password = self.hash_password(password)
        self.manager.register(username, hashed_password)
        self.manager.update_login_track_table(self.manager.select_user_id(username))
        with open('TAN_codes_{}.json'.format(username), 'w') as f:
            json.dump([], f)

    def login_username_check(self):
        username = input('Enter your registered username: ')
        list_of_usernames = self.manager.list_user_names()

        if username not in list_of_usernames:
            print('No such user!')
            return self.login_username_check()

        return username

    def login_password_check(self, name):
        password = getpass.getpass(prompt='Enter your password: ')
        crypted_pass = self.manager.select_password(name)

        if not self.check_password(crypted_pass, password):
            print('Invalid login!')
            client_id = self.manager.select_user_id(name)
            if int(self.manager.select_user_logins(client_id)[1]) != 0:
                print('You are blocked!')
            else:
                self.check_login_attempts(name)

        return password

    def register_failed_attempts(self, name):
        client_id = self.manager.select_user_id(name)
        failure = self.manager.select_user_logins(client_id)[0]
        failure += 1
        self.manager.failed_login_attempts(failure, name)

    def check_login_attempts(self, name):
        client_id = self.manager.select_user_id(name)
        if self.manager.select_user_logins(client_id)[0] == 4:
            self.block_user(name)
        else:
            self.register_failed_attempts(name)

    def block_user(self, name):
        self.manager.time_of_block(time.time(), name)
        self.user_is_suspended = True
        print('Your access for this account is suspended for the next 5 mins!')

    def unblock_user_check(self, name):
        client_id = self.manager.select_user_id(name)
        block_time = self.manager.select_user_logins(client_id)[1]
        if block_time != 0 and time.time() - block_time >= 60:
            self.manager.failed_login_attempts(0, name)
            self.manager.time_of_block(0, name)
            self.user_is_suspended = False

        elif block_time != 0 and time.time() - block_time < 60:
            self.manager.failed_login_attempts(0, name)

    def clear_on_successful_login(self, name):
        self.manager.failed_login_attempts(0, name)
        self.manager.time_of_block(0, name)

    def password_security_check(self, password, username):
        if len(password) <= 8:
            return False

        elif password.islower():
            return False

        elif password.isalnum():
            return False

        elif password.find(username) != -1:
            return False

        count_numbers = 0
        for i in re.findall('\d+', password):
            count_numbers += 1
        if count_numbers == 0:
            return False

        else:
            return True

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()

    def send_email(self, name, content):
        fromaddr = "ivelintod@gmail.com"
        toaddr = self.manager.select_email(name)
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Password reset"
        body = str(content)
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("ivelintod", "82078207")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

    def change_pass_check(self, username):
        new_pass = input('Enter your new password: ')

        if self.password_security_check(new_pass, username):
            return new_pass

        else:
            print('Invalid new password')
            return self.change_pass_check(username)

    def send_reset_password(self):
        name = input('Enter recipient name: ')
        list_of_usernames = self.manager.list_user_names()

        if name not in list_of_usernames:
            print('No such user!')
            self.send_reset_password()

        else:
            self.send_email(name, self.unique_random_code)
            self.recipient = name

    def reset_password(self):
        name = input('Enter username: ')
        if name != self.recipient:
            print('No email was sent to the specified user!')
            self.reset_password()

        else:
            code = input('Enter the code you received in the email: ')
            if self.unique_random_code == code:
                new_pass = self.change_pass_check(name)
                hashed_password = self.hash_password(new_pass)
                client_id = self.manager.select_user_id(name)
                self.manager.reset_pass(hashed_password, client_id)
            else:
                print('Invalid code!')

    def deposit(self, logged_user):
        money = input('Enter amount to deposit: ')

        if money == '':
            print('Invalid amount')
            self.deposit(logged_user)

        elif int(money) < 0:
            print('Invalid amount')
            self.deposit(logged_user)

        else:
            code = input('Enter TAN code: ')
            if code in self.TAN_codes:
                current_balance = logged_user.get_balance()
                updated_balance = current_balance + int(money)
                self.manager.update_balance(updated_balance, logged_user)
                self.update_TAN_codes(code, logged_user)
                print('Successful transaction!\nAmount of {}$ was transfered to your account!'.format(money))
            else:
                print('Invalid TAN code!')

    def withdraw(self, logged_user):
        current_balance = logged_user.get_balance()
        money = input('Enter amount to withdraw: ')

        if money == '':
            print('Invalid amount')
            self.withdraw(logged_user)

        elif int(money) > current_balance:
            print('Invalid amount')
            self.withdraw(logged_user)

        elif int(money) < 0:
            print('Invalid amount')
            self.deposit(logged_user)

        else:
            code = input('Enter TAN code: ')
            if code in self.TAN_codes:
                updated_balance = current_balance - int(money)
                self.manager.update_balance(updated_balance, logged_user)
                self.update_TAN_codes(code, logged_user)
                print('Successful withdrawal!\nAmount of {}$ was withdrawn from your account!'.format(money))
            else:
                print('Invalid TAN code!')

    def update_TAN_codes(self, code, logged_user):
        self.TAN_codes.remove(code)
        with open('TAN_codes_{}.json'.format(logged_user.get_username()), 'w') as f:
            json.dump(self.TAN_codes, f)

    def save_TAN_codes(self, logged_user):
        TAN_codes = []
        for i in range(10):
            unique_code = uuid.uuid4().hex
            TAN_codes.append(unique_code)
        with open('TAN_codes_{}.json'.format(logged_user.get_username()), 'w') as f:
            json.dump(TAN_codes, f)

    def load_TAN_codes(self, logged_user):
        with open('TAN_codes_{}.json'.format(logged_user.get_username()), 'r') as f:
            self.TAN_codes = json.load(f)

    def check_TANs_remaining(self, logged_user):
        count_TAN = 0
        self.load_TAN_codes(logged_user)
        for TAN in self.TAN_codes:
            count_TAN += 1
        return count_TAN == 0

    def get_tan(self, logged_user):
        if self.check_TANs_remaining(logged_user):
            self.save_TAN_codes(logged_user)
            self.load_TAN_codes(logged_user)
            password = input('Enter your password again: ')
            hashed_password = self.manager.select_password(logged_user.get_username())
            if self.check_password(hashed_password, password):
                self.send_email(logged_user.get_username(), self.TAN_codes)
                print("10 unique TAN codes were sent to the provided email.")
            else:
                print('Invalid password!')
                with open('TAN_codes_{}.json'.format(logged_user.get_username()), 'w') as f:
                    json.dump([], f)

        else:
            count_TAN = 0
            for TAN in self.TAN_codes:
                count_TAN += 1
            print('You have {} remaining TAN codes to use'.format(count_TAN))


    def start_command_redirect(self, command):
        if command == 'register':
            self.register_process()
            print('Successful registration')

        elif command == 'login':
            self.login_menu()

        elif command == 'send-reset-password':
            self.send_reset_password()

        elif command == 'reset-password':
            self.reset_password()

    def start_command_inpit(self):
        while True:
            command = input("$$$>")
            if command not in self.start_commands:
                print('Invalid command!')
                self.start_command_inpit()
            else:
                self.start_command_redirect(command)

    def logged_user_command_input(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is: " + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = self.change_pass_check(logged_user.get_username())
                hashed_new_pass = self.hash_password(new_pass)
                self.manager.change_pass(hashed_new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self.manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'change-email':
                new_email = input("Enter your new email: ")
                self.manager.change_email(new_email, logged_user)

            elif command == 'show-email':
                print(logged_user.get_email())

            elif command == 'deposit':
                self.deposit(logged_user)

            elif command == 'withdraw':
                self.withdraw(logged_user)

            elif command == 'show-balance':
                print(str(logged_user.get_balance()) + '$')

            elif command == 'get-tan':
                self.get_tan(logged_user)

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing user message")
                print("show-message - for showing user message")
                print("change-email - for changing user email")
                print("show-email - for showing user email")
                print("deposit - for depositing money into your bank account")
                print("withdraw - for withdrawing money from your bank account")
                print("show-balance - for showing current bank account balance")
                print("get-tan for receiving email with 10 TAN codes for depsit/withdraw")

    def login_menu(self):
        username = self.login_username_check()
        self.unblock_user_check(username)
        if int(self.manager.select_user_logins(self.manager.select_user_id(username))[1]) != 0:
            self.user_is_suspended = True
        else:
            self.user_is_suspended = False
        if self.user_is_suspended:
            print('You are blocked!')
        else:
            password = self.login_password_check(username)
            crypted_pass = self.manager.select_password(username)

            if self.check_password(crypted_pass, password):
                self.clear_on_successful_login(username)
                logged_user = self.manager.login(username)
                self.logged_user_command_input(logged_user)






def main():
    account = Interface()
    account.start_command_inpit()
    #print(time.strftime("%M:%S"))
    #print(time.time())
    #account.save_TAN_codes()
    #account.load_TAN_codes()

if __name__ == '__main__':
    main()
