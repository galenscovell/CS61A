

class Tree:
    """Tree data abstraction.

    >>> Tree(1)
    Tree(1)
    >>> Tree(1, [Tree(0)])
    Tree(1, [Tree(0)])
    """
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        """Modified repr for object representation."""
        if self.branches:
            branches_repr = ', ' + repr(self.branches)
        else:
            branches_repr = ''
        return 'Tree({0}{1})'.format(self.entry, branches_repr)


def square_tree(t):
    """Square all elements of tree."""
    t.entry = t.entry ** 2
    for branch in t.branches:
        square_tree(branch)

def make_even(t):
    """Make all elements of tree even values."""
    if t.entry % 2 != 0:
        t.entry += 1
    for branch in t.branches:
        make_even(branch)

def find_path(t, value):
    """Find path through elements in tree to value."""
    if t.entry == value:
        return [value]
    for branch in t.branches:
        path = find_path(branch, value)
        if path:
            return [t.entry] + path
    return False

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.entry + right.entry, [left, right])