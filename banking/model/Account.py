import string

from banking.model.AccountHolder import AccountHolder


class Account:

    def __init__(self, holder: AccountHolder, account_number, pin: string, starting_deposit: float):
        self.account_holder = holder
        self.account_number = account_number
        self.pin = pin
        self.deposit = starting_deposit

    def validate_pin(self, attempt_pin):
        return self.pin == attempt_pin

    def credit_account(self, amount):
        pass

    def debit_account(self, amount):
        pass
