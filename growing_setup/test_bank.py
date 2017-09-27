import unittest

from growing_setup.account import Account
from growing_setup.bank import Bank


class BankTests(unittest.TestCase):
    def assertMoneyEquals(self, expected, actual):
        self.assertEqual(expected, actual)


class BankContext(BankTests):
    @classmethod
    def setUpClass(cls):
        cls.starting_rate = 0.0025
        Bank.standard_rate = cls.starting_rate


class NewAccountContext(BankContext):
    def setUp(self):
        self.new_account = Account()

    def test_upon_new_account_balance_will_be_zero(self):
        self.assertMoneyEquals(0, self.new_account.balance)

    def test_upon_new_account_has_standard_interest_rate(self):
        self.assertMoneyEquals(Bank.standard_rate, self.new_account.interest_rate)


class OldAccountContext(BankContext):
    def setUp(self):
        self.old_account = Account()

    def test_should_have_old_interest_rate(self):
        self.assertMoneyEquals(self.starting_rate, self.old_account.interest_rate)


class AfterInterestRateContext(BankContext):
    @classmethod
    def setUpClass(cls):
        cls.new_rate = 0.0035
        Bank.standard_rate = cls.new_rate

    def setUp(self):
        self.new_account = Account()

    def test_when_rate_changes_old_account_keeps_old_rate(self):
        self.assertMoneyEquals(self.new_rate, self.new_account.interest_rate)