import statement


class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def statement(self):
        return statement.Statement(self._rentals, self._name)
