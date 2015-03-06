
# Set literals are enclosed in braces
# Duplicate elements are removed on construction
# Sets are unordered


# Python built-in sets
s1 = {1, 2, 3, 4}
s2 = {1, 5}
s3 = {6, 5, 4, 3}
def set_union(s1, s2):
    """Return all elements within both set1 and set2.
    >>> set_union(s1, s2)
    {1, 2, 3, 4, 5}
    """
    return s1.union(s2)

def set_intersection(s1, s2):
    """Return elements in common between set1 and set2.
    >>> set_intersection(s1, s3)
    {3, 4}
    """
    return s1.intersection(s3)



# Implementing sets as binary search trees
# A set is represented as a tree with two branches
# Each entry is larger than all entries in its left branch
#   and smaller than all entries in its right branch
# Each binary tree always has exactly two branches 
#   (either other trees or empty)

from TreeClass import Tree

class BinaryTree(Tree):
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left=empty, right=empty):
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]
    
Bin = BinaryTree
t = Bin(3, Bin(1),
           Bin(7, Bin(5),
                  Bin(9, Bin.empty,
                         Bin(11))))

def tree_set_contains(s, v):
    if s.is_empty:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return tree_set_contains(s.right, v)
    elif s.entry > v:
        return tree_set_contains(s.left, v)

def tree_adjoin_set(s, v):
    """
    Check branches and choose left or right for proper placement.
    """
    if s.is_empty:
        return Bin(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Bin(s.entry, s.left, tree_adjoin_set(s.right, v))
    elif s.entry > v:
        return Bin(s.entry, tree_adjoin_set(s.left, v), s.right)




# Implementing sets as unordered sequences
# A set is represented as a linked list with no duplicates

from LinkedListClass import *

def empty(s):
    return s is Link.empty

def link_set_contains(s, v):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> set_contains(s, 2)
    True
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return link_set_contains(s.rest, v)

def link_adjoin_set(s, v):
    if link_set_contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect_set(set1, set2):
    in_set2 = lambda v: link_set_contains(set2, v)
    return keep_if(set1, in_set2)

def union_set(set1, set2):
    not_in_set2 = lambda v: not link_set_contains(set2, v)
    set1_not_set2 = keep_if(set1, not_in_set2)
    return extend(set1_not_set2, set2)