from banking.model.AccountHolder import AccountHolder


class Person(AccountHolder):

    def __init__(self, first_name, last_name, id_number):
        super().__init__(id_number)
        self.first_name = first_name
        self.last_name = last_name

