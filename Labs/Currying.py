
def curried_pow(x):
    """Curried version of raising x to the y power."""
    def h(y):
        return pow(x, y)
    return h

def curry2(f):
    """Return curried version of given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """Return two-argument version of given function."""
    def f(x, y):
        return g(x)(y)
    return f

