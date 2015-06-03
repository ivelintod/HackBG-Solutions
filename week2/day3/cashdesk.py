class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        message = 'A {}$ bill'
        return message.format(self.amount)

    def __repr__(self):
        return 'A {}$ bill'.format(self.amount)

    def __eq__(self, other):
        return self.amount == other

    def __hash__(self):
        return hash(self.amount)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        total = 0
        for bill in self.bills:
            total += 1
        return total

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:

    def __init__(self):
        self.vault = []

    def take_money(self, money):
        if isinstance(money, BatchBill):
            self.vault += [int(bill) for bill in money]
        elif isinstance(money, Bill):
            self.vault.append(int(money))

    def total(self):
        total = 0
        for money in self.vault:
            total += money
        return total

    def inspect(self):
        diff_bills = []
        for bill in self.vault:
            if bill not in diff_bills:
                diff_bills.append(bill)
        for bill in diff_bills:
            print('{}$ bills - {}'.format(bill, self.vault.count(bill)))


bills = [Bill(10), Bill(20), Bill(50), Bill(100)]
batch = BatchBill(bills)
for bill in batch:
    print(bill)

desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())
desk.inspect()


