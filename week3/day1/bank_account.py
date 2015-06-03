class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        if balance < 0:
            raise ValueError
        else:
            self.balance = balance
        self.currency = currency
        self.history = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount
            self.history.append('Deposited {}{}'.format(amount, self.currency))

    def current_balance(self):
        self.history.append('Balance check -> {}'.format(self.balance))
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
            return False
            self.history.append("Withdraw for invalid amount failed")
        elif self.balance - amount > 0:
            self.balance -= amount
            self.history.append("{}{} was withdrawn".format(amount, self.currency))
            return True
        else:
            raise ValueError

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def __int__(self):
        return self.balance

    def transfer_to(self, account, amount):
        if amount < 0:
            raise ValueError
            return False
        else:
            if self.currency == account.currency:
                if self.balance - amount >0:
                    account.balance += amount
                    self.balance -= amount
                    self.history.append("Transfer to {} for {}{}".format(account.name, amount, self.currency))
                    account.history.append("Transfer from {} for {}{}".format(self.name, amount, self.currency))
                    return True
                else:
                    raise ValueError
                    return False
            else:
                return False

    def account_history(self):
        return self.history


rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
print(rado.current_balance())
print(ivo.current_balance())
print(rado.account_history())
print(ivo.account_history())
