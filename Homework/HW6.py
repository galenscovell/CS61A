
# Question One
class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.cash = 0
        self.stock = 0

    def restock(self, amount):
        if amount > 0:
            self.stock += amount
            return "Current " + self.product + " stock: " + str(self.stock)
        else:
            return "Restock amount must be positive!"

    def deposit(self, amount):
        if amount > 0:
            if self.stock == 0:
                return "Machine is out of stock. Here is your $" + str(amount)
            else:
                self.cash += amount
                return "Current balance: $" + str(self.cash)
        else:
            return "Deposit amount must be positive!"

    def vend(self):
        if self.stock == 0:
            return "Machine is out of stock."
        else:
            if self.cash < self.price:
                difference = self.price - self.cash
                return "You must deposit $" + str(difference) + " more."
            elif self.cash > self.price:
                difference = self.cash - self.price
                self.stock -= 1
                self.cash = 0
                return "Here is your " + self.product + " and $" + str(difference) + " change."
            elif self.cash == self.price:
                self.stock -= 1
                return "Here is your " + self.product + "."




# Question Two
class MissManners(object):
    """A container class that only forwards messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        if message[:6] == 'please':
            method = message[7:]
            if hasattr(self.obj, method):
                return getattr(self.obj, method)(*args)
            else:
                return "Thanks for asking, but I know not how to " + str(method) + "."
        else:
            return "You must learn to say please."