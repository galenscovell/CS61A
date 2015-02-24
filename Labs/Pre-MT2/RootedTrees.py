
# Rooted trees have a value at the root of every tree
# Rooted tree with zero branches is a leaf
# Root values of sub-trees within rooted tree are called nodes


def rooted(value, branches):
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

from operator import add, mul
def eval_tree(tree):
    """Evaluates expression tree with function as root."""
    if is_leaf(tree):
        return root(tree)
    fn = root(tree)
    values = branches(tree)
    print(fn, values)
    if fn is add:
        start = 0
    else:
        start = 1
    return reduce(fn, apply_to_all(eval_tree, values), start)