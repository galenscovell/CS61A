
def reverse_iter(lst):
    """Returns reverse of given list, iteratively."""
    if len(lst) == 0:
        return lst
    reversed_lst = []
    while len(lst) > 0:
        reversed_lst.append(lst[-1])
        del lst[-1]
    return reversed_lst


def reverse_recursive(lst):
    """Returns reverse of given list, recursively."""
    if not lst:
        return lst
    return reverse_recursive(lst[1:]) + [lst[0]]


def deep_len(lst):
    """Returns deep length of given list."""
    if not lst:
        return 0
    elif type(lst[0]) is list:
        return deep_len(lst[0]) + deep_len(lst[1:])
    else:
        return 1 + deep_len(lst[1:])


def merge(lst1, lst2):
    """Merges two sorted lists recursively."""
    if not lst1 or not lst2:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])


def mergesort(seq):
    """Mergesort algorithm, recursive."""
    if len(seq) < 2:
        return seq
    middle = len(seq) // 2
    return merge(mergesort(seq[:middle]), mergesort(seq[middle:]))


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]


def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]