

class Bank:
    cash = 100000000

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    @classmethod
    def borrow(cls, bank):
        amount = int(input("Amount : "))
        bank.add_cash(amount)
        cls.cash -= amount

    def deposit(self):
        pass

    def withdraw(self):
        pass


class KBZ(Bank):
    def __init__(self, name, branch):
        super().__init__(name, branch)
        self.cash = 0

    def set_cash(self, cash):
        self.cash = cash

    def location(self):
        return "Mandalay"

    def add_cash(self, cash):
        self.cash = self.cash + cash


kbz = KBZ("KBZ", 3)
kbz.set_cash(200000000)
Bank.borrow(kbz)
print(kbz.cash)
