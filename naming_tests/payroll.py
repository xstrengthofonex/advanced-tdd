

class Employee(object):
    def __init__(self, name):
        self.name = name
        self.pay_type = None
        self.disposition = None
        self.pay_day = "Friday"


class HourlyPayType(object):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.time_cards = []

    def add_time_card(self, time_card):
        self.time_cards.append(time_card)

    def calculate_pay(self):
        total_amount = 0.0
        for time_card in self.time_cards:
            total_amount += time_card.hours_worked * self.hourly_rate
        return total_amount


class Check(object):
    def __init__(self, amount):
        self.amount = amount


class PayMaster(object):
    def __init__(self):
        self.held_pay_checks = []

    def get_held_pay_checks(self):
        return self.held_pay_checks

    def pay(self, check):
        self.held_pay_checks.append(check)


class TimeCard(object):
    def __init__(self, hours_worked):
        self.hours_worked = hours_worked


class Payroll(object):
    def __init__(self):
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def run(self, date):
        for employee in self.employees:
            if employee.pay_day == date.strftime("%A"):
                total_amount = employee.pay_type.calculate_pay()
                employee.disposition.pay(Check(total_amount))



