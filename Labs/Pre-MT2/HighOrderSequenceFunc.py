
def apply_to_all(map_fn, s):
    """
    Apply map_fn to each element of s.
    [Called MAP in most languages]

    >>> apply_to_all(lambda x: x * 3, range(5))
    [0, 3, 6, 9, 12]
    """
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    """
    List all elements x of s for which filter_fn(x) is true.
    [Called FILTER in most languages]

    >>> keep_if(lambda x: x > 5, range (10))
    [6, 7, 8, 9]
    """
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    """
    Combine elements of s pairwise using reduce_fn, starting with initial.
    [Called REDUCE or ACCUMULATE in most languages]

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    167777216
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced