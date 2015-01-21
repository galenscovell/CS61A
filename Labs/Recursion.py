
def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive."""
    if n == 1:
        return 1
    return n + sum(n - 1)

def sum_every_other(n):
    """Return sum of every other natural number up to n, inclusive."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_every_other(n - 2)

def fib(n):
    """Return nth fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def hailstone(n):
    """If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1."""
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner."""
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)