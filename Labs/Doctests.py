
# python -m doctest [file]      only show failed output
# python -m doctest -v [file]   show all output


def gcd(m, n):
    """
    Returns largest k that divides evenly into m and n.
    k, m, n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(5, 5)
    5
    """
    if n % m == 0:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m - n, n)