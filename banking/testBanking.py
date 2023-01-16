import unittest

from banking.entity.Company import Company
from banking.entity.Person import Person
from banking.model.Bank import Bank


class MyTestCase(unittest.TestCase):
    john = Person("john", "kennedy", 1)
    julia = Person("julia", "singh", 2)
    daniel = Person("daniel", "radcliffe", 3)
    company_ibm = Company("IBM", 1)
    company_ford = Company("Ford", 2)
    account_john = None
    account_julia = None
    account_daniel = None
    account_ibm = None
    account_ford = None
    bank = Bank()

 #   def set_up(self):

 #       account_john = self.bank.openConsumerAccount(self.john, 1111, 0.0)
 #       account_julia = self.bank.openConsumerAccount(self.julia, 2222, 456.78)
 #       account_daniel = self.bank.openConsumerAccount(self.daniel, 3333, 500.00)
 #       account_ibm = self.bank.openCommercialAccount(self.company_ibm, 1111, 0.0)
 #       account_ford = self.bank.openCommercialAccount(self.company_ford, 2222, 123456789.00)

    def test_debit_personal_account(self):
        bank = Bank()
        julia = Person("julia", "singh", 2)
        account_julia = bank.open_customer_account(julia, 2222, 456.78)
        debit_amount = 34.0
        balance_init = bank.get_account_balance(account_julia)
        bank.debit(account_julia, debit_amount)
        balance_left = bank.get_account_balance(account_julia)
        self.assertEqual(balance_init, balance_left+debit_amount, f"Init balance is {balance_init}, current balance is {balance_left}")


if __name__ == '__main__':
    unittest.main()
