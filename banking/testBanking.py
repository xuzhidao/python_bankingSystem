import unittest

from banking.entity.Company import Company
from banking.entity.Person import Person
from banking.entity.Transaction import Transaction, InvalidPinError
from banking.model.Account import InsufficientBalanceError
from banking.model.Bank import Bank


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setup testing context')
        self.bank = Bank()
        self.julia = Person("julia", "singh", 2)
        self.john = Person("john", "kennedy", 1)
        self.julia = Person("julia", "singh", 2)
        self.daniel = Person("daniel", "radcliffe", 3)
        self.company_ibm = Company("IBM", 1)
        self.company_ford = Company("Ford", 2)
        self.account_john = self.bank.open_customer_account(self.john, 1111, 0.0)
        self.account_julia = self.bank.open_customer_account(self.julia, 2222, 456.78)
        self.account_daniel = self.bank.open_customer_account(self.daniel, 3333, 500.00)
        self.account_ibm = self.bank.open_commercial_account(self.company_ibm, 'ibm-pin-123', 0.0)
        self.account_ford = self.bank.open_commercial_account(self.company_ford, 'ford-pin-345', 123456789.00)

    def tearDown(self):
        print('tearDown')

    def test_debit_personal_account(self):
        print('Test debit personal account')
        debit_amount = 34.0
        balance_init = self.bank.get_account_balance(self.account_julia)
        self.bank.debit(self.account_julia, debit_amount)
        balance = self.bank.get_account_balance(self.account_julia)
        self.assertEqual(balance_init, balance+debit_amount, f"Init balance is {balance_init}, current balance is {balance}")

    def test_debit_personal_account_insufficient(self):
        print('Test debit personal account')
        debit_amount = 34.0
        balance_init = self.bank.get_account_balance(self.account_john)
        try:
            self.bank.debit(self.account_john, debit_amount)
        except InsufficientBalanceError:
            self.assertTrue(True, 'Exception captured')
        self.fail('Test failed, should throw error')

    def test_credit_personal_account(self):
        print('Test credit personal account')
        credit_amount = 31.0
        balance_init = self.bank.get_account_balance(self.account_julia)
        self.bank.credit(self.account_julia, credit_amount)
        balance = self.bank.get_account_balance(self.account_julia)
        self.assertEqual(balance_init, balance+credit_amount, f"Init balance is {balance_init}, current balance is {balance}")

    def test_transaction_invalid_pin(self):
        print('Test invalid pin')

        try:
            txn = Transaction(self.bank,self.account_john,'welcome')
        except InvalidPinError:
            self.assertTrue(True, 'Exception captured')
        self.fail('Test failed, should throw error')

    if __name__ == '__main__':
        unittest.main()
