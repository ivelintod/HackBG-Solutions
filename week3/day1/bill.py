class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return str(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount
