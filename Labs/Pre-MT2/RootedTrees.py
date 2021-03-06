
# Rooted trees have a value at the root of every tree
# Rooted tree with zero branches is a leaf
# Root values of sub-trees within rooted tree are called nodes


def rooted(value, branches=[]):
    for branch in branches:
        assert is_rooted(branch)
    return [value] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def leaf(value):
    return rooted(value, [])

def is_leaf(tree):
    return type(tree) != list

def is_rooted_leaf(tree):
    return branches(tree) == []

def is_rooted(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_rooted(branch):
            return False
    return True

# >>> t = rooted(1, [leaf(2), leaf(3)])
# >>> t
# [1, [2], [3]]
# >>> root(t)
# 1
# >>> branches(t)
# [[2], [3]]


def fib_tree(n):
    if n == 0 or n == 1:
        return rooted(n, [])
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        root_value = root(left) + root(right)
        return rooted(root_value, [left, right])




def reduce(fn, s, init):
    reduced = init
    for x in s:
        reduced = fn(reduced, x)
    return reduced

def apply_to_all(fn, s):
    return [fn(x) for x in s]



def hailstone_tree(n, height):
    """Generates rooted tree of hailstone sequence reaching N with HEIGHT.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if height == 0:
        return rooted(n)
    branches = [hailstone_tree(n * 2, height - 1)]
    if (n - 1) % 6 == 3 and (n - 1) // 3 > 1:
        branches += [hailstone_tree((n - 1) // 3, height - 1)]
    return rooted(n, branches)


def find_path(tree, x):
    """Return path in tree to leaf with value X, None if leaf not present in tree.
    >>> t = rooted(2, [rooted(7, [leaf(3), rooted(6, [leaf(5), leaf(11)])]), leaf(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 6)
    [2, 7, 6]
    >>> find_path(t, 10)
    False
    """
    if root(tree) == x:
        return [root(tree)]
    node, trees = root(tree), branches(tree)
    for path in [find_path(t, x) for t in trees]:
        if path:
            return [node] + path