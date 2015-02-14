
from operator import add

def keep_if(filter_fn, s):
    """List all elements x of s for which filter_fn(x) is true."""
    return [x for x in s if filter_fn(x)]

def divisors(n):
    """Returns divisors of n."""
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def reduce(reduce_fn, s, initial):
    """Combine elements of s pairwise using reduce_fn, starting with initial."""
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def sum_divisors(n):
    """Return sum of all of n's divisors."""
    return reduce(add, divisors(n), 0)

def perfect(n):
    """Return if n is a 'perfect' number (sum of divisors == n)."""
    return sum_divisors(n) == n