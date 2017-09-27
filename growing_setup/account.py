from growing_setup.bank import Bank


class Account(object):
    def __init__(self):
        self.balance = 0
        self.interest_rate = Bank.standard_rate

