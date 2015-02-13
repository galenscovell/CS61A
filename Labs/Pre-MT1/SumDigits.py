
def sum_digits(n):
    """Return sum of the digits composing positive integer n."""
    if n < 10:
        return n
    else:
        last, all_but_last = n % 10, n // 10
        return last + sum_digits(all_but_last)