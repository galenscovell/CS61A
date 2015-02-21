
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

def is_rooted(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_rooted(branch):
            return False
    return True

# rooted(3, [rooted(1, []),
#            rooted(2, [rooted(1, []),
#                       rooted(1, [])])])
# => [3, [1], [2, [1], [1]]]


def fib_tree(n):
    if n == 0 or n == 1:
        return rooted(n, [])
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        root_value = root(left) + root(right)
        return rooted(root_value, [left, right])
