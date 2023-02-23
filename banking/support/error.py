class InvalidAccountError(Exception):

    def __init__(self, salary, message="Account suspended"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


class TransactionNotAllowedError(Exception):

    def __init__(self, salary, message="Traction not allowed"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
