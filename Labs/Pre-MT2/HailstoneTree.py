
from TreeClass import Tree


def hailstone_tree(length, n=1):
    """Build tree in which paths are hailstone sequences."""
    if length == 1:
        return Tree(n)
    else:
        above, below = 2 * n, (n - 1) / 3
        branches = [hailstone_tree(length - 1, above)]
        if below > 1 and is_int(below) and is_odd(below):
            branches.append(hailstone_tree(length - 1, int(below)))
        return Tree(n, branches)


def is_int(x):
    returnt int(x) == x

def is_odd(n):
    return n % 2 == 1