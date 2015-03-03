

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


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.entry + right.entry, [left, right])