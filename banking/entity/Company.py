from banking.model.AccountHolder import AccountHolder


class Company(AccountHolder):

    def __init__(self, company_name, id_number):
        self.company_name = company_name
        super().__init__(id_number)
