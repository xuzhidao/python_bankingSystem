from banking.entity.Person import Person
from banking.model import AccountHolder
from banking.model import Account


class CommercialAccount(Account):

    def __init__(self, company: AccountHolder, account_number, pin, starting_deposit: float):
        super().__init__(company, account_number, pin, starting_deposit)
        self.authorized_users = []

    # *
    #      * @param person The authorized user to add to the account.
    def add_authorized_user(self, person: Person):
        self.authorized_users.append(person)

    # *
    #      * @param person
    #      * @return true if person matches an authorized user in {@link #authorizedUsers}; otherwise, false.
    def is_authorized_user(self, person: Person):
        for user in self.authorized_users:
            if user.id_number == person.id_number:
                return True
        return False
