from banking.model import Bank


class Transaction:

    def __init__(self, bank: Bank, account_number, attempt_pin):
        self.bank = bank
        self.account_number = account_number
        if bank.authenticate_user(account_number, attempt_pin):
            raise UnauthenticatedUser();

    def get_balance(self):
        # complete the function
        return self.bank.get_account_balance(self.account_number)

    def credit(self, amount):
        self.bank.credit(self.account_number, amount)

    def debit(self, amount):
        # if balance is not enough, throw exception
        pass


class InvalidPinError:
    def __init__(self):
        pass
