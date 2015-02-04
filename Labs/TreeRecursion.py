
def count_stair_ways(n):
    """Counts ways of ascending staircase composed of n steps using either 1 or 2 steps."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def pascal(row, column):
    """Calculates value in pascal triangle at row and column."""
    if row < 0 or column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)


def has_sum(sum_val, n1, n2):
    """Returns true if multiples of n1 and n2 can sum to be SUM.
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """
    if sum_val == n1 or sum_val == n2:
        return True
    if sum_val < min(n1, n2):
        return False
    return has_sum(sum_val - n1, n1, n2) or has_sum(sum_val - n2, n1, n2)
