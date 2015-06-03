class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def deposit(self, amount):

        if amount < 0:
            raise ValueError

        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError

        self.balance -= amount

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError

        if self.balance < amount:
            return False

        self.withdraw(amount)
        account.deposit(amount)
        #self.balance = amount
        #account.balance = amount
        return True

    '''def history(self):
        list_history = []
        if account == BankAccount:
            list_history.append("Account was created")
        if account.balance != BankAccount.balance:
            acc_b = account.balance()
            list_history.append("Deposited " + str(acc_b) + "$")
            list_history.append("Balance check ->" + str(acc_b) + "$")
        return list_history'''


account = BankAccount("Rado", 0, "$")
account.deposit(1000)
#print (account.history())
