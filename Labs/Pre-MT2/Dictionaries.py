
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

