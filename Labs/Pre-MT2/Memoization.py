
# Memoization: remember results that have already been computed


def count(f):
    """Count number of calls to function."""
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)

"""
>>> fib = count(fib)
>>> fib(10)
34
>>> fib.call_count
109
"""



def memo(f):
    """Return a memoized version of single-argument function f."""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


"""
>>> fib = count(fib)
>>> counted_fib = fib
>>> fib = memo(fib)
>>> fib = count(fib)
>>> fib(10)
34
>>> fib.call_count
17
"""