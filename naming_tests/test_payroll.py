import unittest
from datetime import date

from naming_tests.payroll import PayMaster, HourlyPayType, Employee, TimeCard, Payroll


class PayrollTest(unittest.TestCase):
    pass


class GivenEmployee(PayrollTest):
    def setUp(self):
        self.employee = Employee("Employee")


class GivenHourlyPayTypeEarningStandardRate(GivenEmployee):
    standard_hourly_rate = 10.0

    def setUp(self):
        super().setUp()
        self.hourly_pay_type = HourlyPayType(self.standard_hourly_rate)
        self.employee.pay_type = self.hourly_pay_type


class GivenTimeCardsAddUpToLessThanOvertime(GivenHourlyPayTypeEarningStandardRate):
    days_per_week = 5
    max_regular_hours_per_day = 8

    def setUp(self):
        super().setUp()
        for day in range(self.days_per_week):
            self.hourly_pay_type.add_time_card(TimeCard(self.max_regular_hours_per_day))


class GivenPayDisposition(GivenTimeCardsAddUpToLessThanOvertime):
    def setUp(self):
        super().setUp()
        self.employee.disposition = PayMaster()


class GivenTodayIsFriday(GivenPayDisposition):
    def setUp(self):
        super().setUp()
        self.today = date(2013, 8, 9)

    def test_when_payroll_is_run_then_paymaster_will_hold_check_for_hours_worked_times_hourly_rate(self):
        payroll = Payroll()
        payroll.add(self.employee)
        payroll.run(self.today)
        pay_master = self.employee.disposition
        checks = pay_master.get_held_pay_checks()
        self.assertEqual(1, len(checks))
        check = checks[0]
        self.assertEqual(self.standard_hourly_rate * self.max_regular_hours_per_day * self.days_per_week,
                         check.amount)
