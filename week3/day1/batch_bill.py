class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __getitem__ (self, index):
        return self.bills[index]
