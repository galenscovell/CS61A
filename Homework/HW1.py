
# Question One
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a + abs(b) without calling abs."""
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


# Question Two
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest positive numbers of a, b, and c."""
    def square(x):
        return x * x
    if a >= b >= c:
        n, m = a, b
    elif c >= b >= a:
        n, m = b, c
    else:
        n, m = a, c
    return square(n) + square(m)


# Question Three
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

"""Write functions which make with_if_statement return 1, but with_if_function return false value"""
def c():
    return False

def t():
    return 0

def f():
    return 1


# Question Four
def hailstone(n):
    """Print hailstone sequence starting at n length."""
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
