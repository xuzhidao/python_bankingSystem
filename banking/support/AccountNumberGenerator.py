import random


class AccountNumberGenerator:
    company_sections = 4
    account_seperator = '-'
    personal_sections = 3
    account_num = ''

    def __init__(self):
        pass

    def generate_company_account_number(self, company):
        for x in range(self.company_sections):
            self.account_num += str(random.randint(1000, 9999))
            if x == (self.company_sections - 1):
                self.account_num += str(random.randint(1000, 9999))
            else:
                self.account_num += str(random.randint(1000, 9999)) + self.account_seperator
        return self.account_num

    def generate_personal_account_number(self, person):
        pass
