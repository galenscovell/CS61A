
# Dictionaries:
    # are unordered
    # keys cannot be lists or dictionaries
    # two keys cannot be equal


def create_dict_squares(limit):
    """
    Use dictionary comprehension to create dict with squares up to limit.

    >>> create_dict_squares(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    squares = {x:x*x for x in range(limit)}
    return squares


def replace_all(d, x, y):
    """Replace all occurences of x as a value (not a key) with y."""
    for key in d:
        if d[key] == x:
            d[key] = y


def replace_all_deep(d, x, y):
    """Given arbitrarily deep dictionary d, replace all occurences of 
    x as a value (not a key) with y.
    >>> d = {1: {2: 3, 3: 4}, 2: {4: 4, 5: 3}}
    >>> replace_all(d, 3, 1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """
    for key in d:
        if type(d[key]) is dict:
            replace_all(d[key], x, y)
        else:
            if d[key] == x:
                d[key] = y

