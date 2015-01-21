
def square(x):
    return x * x
def triple(x):
    return 3 * x
def identity(x):
    return x
def increment(x):
    return x + 1
def negate(x):
    return -x

# Question One
def piecewise(f, g, b):
    """Returns piecewise function h where
        h(x) = f(x) if x < b,
        h(x) = g(x) otherwise
    """
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h


# Question Two
def intersects(f, x):
    """Returns function that returns whether f intersects g at x."""
    def h(g):
        return f(x) == g(x)
    return h
        

# Question Three
def repeated(f, n):
    """Return the function that computes the nth application of f."""
    def h(x):
        value = x
        for y in range(1, n + 1):
            value = f(value)
        return value
    return h
