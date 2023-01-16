from banking.model.Account import Account
from banking.model import AccountHolder


class CustomerAccount(Account):

    def __init__(self, person: AccountHolder, account_number, pin, starting_deposit: float):
        super().__init__(person, account_number, pin, starting_deposit)
