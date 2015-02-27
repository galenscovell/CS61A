
# Nonlocal: future assignments to that name change its pre-existing binding 
# in the first non-local frame of the current environment in which that names 
# is bound.


# Mutable values/functions violate referential transparency 
# because they do more than just return a value, they change the environment.



def make_withdraw(balance):
    """Return withdraw function with starting balance."""
    def withdraw(amount):
        # Look for 'balance' outside of scope
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds.'
        balance -= amount
        return balance
    return withdraw


def f(x):
    """
    >>> a = f(1)
    >>> b = a(2)
    >>> b(3) + b(4)
    22
    """
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x += 1
            return x + x + z
        return h
    return g