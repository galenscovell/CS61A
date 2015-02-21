
# Tree processing uses recursion.
# Base case: process single leaf
# Recursive case: recursive call on each branch, then aggregation


tree = [[1, [2], 3, []], [[4], [5, 6]], 7]

def is_leaf(tree):
    """Returns if tree is a leaf (anything but a list)."""
    return type(tree) != list

def count_leaves(tree):
    """Counts number of leaves in tree."""
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in tree]
        return sum(branch_counts)

def flatten(tree):
    """
    Return list containing leaves of tree.

    >>> tree = [[1, [2], 3, []], [[4], [5, 6]], 7]
    >>> flatten(tree)
    [1, 2, 3, 4, 5, 6, 7]
    """
    if is_leaf(tree):
        return [tree]
    else:
        # Flatten each branch, then aggregate them
        return sum([flatten(b) for b in tree], [])

def apply_to_leaves(map_fn, tree):
    """Apply map_fn to all leaves of tree, constructing another tree."""
    if is_leaf(tree):
        return map_fn(tree)
    else:
        return [apply_to_leaves(map_fn, branch) for branch in tree]




# Binary Trees
# Binary tree is a leaf/sequence containing at most two binary trees (two branches)
# Binarization: Tree -> Binary Tree

def right_binarize(tree):
    """
    Construct a right-branching binary tree.

    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    """
    if is_leaf(tree):
        return tree
    elif len(tree) > 2:
        # All but first branch grouped into new branch
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

pangram = [['the', 'quick', 'brown', 'fox'], ['jumps', 'over', 'a', 'lazy', 'dog']]