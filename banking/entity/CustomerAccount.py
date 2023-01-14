from banking.model import Account, AccountHolder


class CustomerAccount(Account):

    def __init__(self, person: AccountHolder, account_number, pin, starting_deposit: float):
        super().__init__(person, account_number, pin, starting_deposit)
