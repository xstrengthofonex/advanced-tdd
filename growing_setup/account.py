from growing_setup.bank import Bank


class Account(object):
    def __init__(self) -> None:
        self.balance: int = 0
        self.interest_rate: float = Bank.standard_rate

