class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

def test():
    a1 = BankAccountP('John', 'Olsson', '10', 100)
    a2 = BankAccountP('Liz', 'Olsson',  '20', 200)
    assert 100 == a1.get_balance()
    assert 200 == a2.get_balance()
    a1.transfer(a2, 50)
    assert 50 == a1.get_balance()
    assert 250 == a2.get_balance()
    a2.transfer(a1, 100)
    assert 150 == a1.get_balance()
    assert 150 == a2.get_balance()

test()
