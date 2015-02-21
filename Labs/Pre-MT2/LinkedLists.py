
# Linked list with length 1
one = [1, 'empty']
# Linked list with length 2
two = [1, [2, 'empty']]
# Linked list with length 4
four = [1, [2, [3, [4, 'empty']]]]



def is_link(s):
    """s is linked list if it is empty or a (first, rest) pair."""
    return s == 'empty' or (type(s) == list and len(s) == 2 and is_link(s[1]))

# Constructor:
def link(first, rest):
    """Construct linked list from first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

# Selectors:
def first(s):
    """Returns first element of linked list s."""
    assert is_link(s), 'first only applies to linked list.'
    assert s != 'empty', 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Returns rest of elements of linked list s."""
    assert is_link(s), 'rest only applies to linked list.'
    assert s != 'empty', 'empty linked list has no rest.'
    return s[1]



def len_link_i(s):
    """Return length of linked list s, iteratively."""
    length = 0
    while s != 'empty':
        s, length = rest(s), length + 1
    return length

def len_link_r(s):
    """Return length of linked list s, recursively."""
    if s == 'empty':
        return 0
    else:
        return 1 + len_link(rest(s))

def get_item_i(s, i):
    """Return element at index i of linked list s, iteratively."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def get_item_r(s, i):
    """Return element at index i of linked list s, recursively."""
    if i == 0:
        return first(s)
    else:
        return get_item(rest(s), i - 1)



def extend(s, t):
    """
    >>> extend(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    """
    if s == 'empty':
        return t
    else:
        return link(first(s), extend(rest(s), t))

def reverse(s):
    return reverse_to(s, 'empty')

def reverse_to(s, t):
    """
    >>> reverse(four)
    [4, [3, [2, [1, 'empty']]]]
    """
    if s == 'empty':
        return t
    else:
        return reverse_to(rest(s), link(first(s), t))

def apply_to_all(f, s):
    """
    >>> apply_to_all(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    if s == 'empty':
        return 'empty'
    else:
        return link(f(first(s)), apply_to_all(f, rest(s)))



def partitions(n, m):
    """
    Return linked list of the partitions of integer n using parts up to m. 
    Each partition is a linked list of numbers.
    """
    if n == 0:
        return link('empty', 'empty')
    elif n < 0:
        return 'empty'
    elif m == 0:
        return 'empty'
    else:
        # Do we use at least one m?
        yes = partitions(n - m, m)
        no = partitions(n, m - 1)
        add_m = lambda s: link(m, s)
        with_m = apply_to_all(add_m, yes)
        return extend(with_m, no)

def join(s, separator):
    if s == 'empty':
        return ''
    elif rest(s) == 'empty':
        return str(first(s))
    else:
        return str(first(s)) + separator + join(rest(s), separator)

def print_partitions(n, m):
    links = partitions(n, m)
    strings = apply_to_all(lambda s: join(s, ' + '), links)
    print(join(strings, '\n'))