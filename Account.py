class Account(object):

    def __init__(self):
        self._quantity = 0
        self._balance = 100000.00
        self._balances = []

    def buy(self, symbol, quantity, price):
        self._quantity += quantity

        self._balance -= price * quantity
        self._balances.append(self._balance)

    def sell(self, symbol, quantity, price):
        self._quantity -= quantity
            
        self._balance += price * quantity
        self._balances.append(self._balance)

    def liquidate(self, symbol, price):
            if self._quantity > 0:
                self.sell(symbol, self._quantity, price)
            elif self._quantity < 0:
                self.buy(symbol, -self._quantity, price)


    