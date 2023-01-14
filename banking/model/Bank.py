from banking.entity import CommercialAccount, CustomerAccount


class Bank:

    def __init__(self):
        self.accounts = {}

    def get_account(self, account_number):
        return self.accounts[account_number]

    def open_commercial_account(self, company, pin, starting_deposit):
        commercial_account = CommercialAccount(company, 45, pin, starting_deposit)
        self.accounts[commercial_account.account_number] = commercial_account
        return commercial_account.account_number

    def open_customer_account(self, person, pin, starting_deposit):
        customer_account = CustomerAccount(person, 45, pin, starting_deposit)
        self.accounts[customer_account.account_number] = customer_account
        return customer_account.account_number

    def authenticate_user(self, account_number, pin):
        account = self.accounts[account_number]
        if account is None:
            return False
        if account.pin != pin:
            return False
        return True

    def get_account_balance(self, account_number):
        account = self.accounts[account_number]
        if account is None:
            return 0.0
        return account.deposit

    def credit(self, account_number, amount):
        pass

    def debit(self, account_number, amount):
        pass