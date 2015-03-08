
# Linked List class
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        """Gets value at index i using link[i] notation."""
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __setitem__(self, i, value):
        """Sets value at index i using link[i] notation."""
        if index == 0:
            self.first = value
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[i - 1] = value

    def __len__(self):
        """Returns number of items in Link."""
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        """Returns a human-readable string representation of Link."""
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

    def __add__(self, other):
        """Adds two Links using normal + notation."""
        ret = Link.empty
        while self is not Link.empty:
            ret = Link(self.first, ret)
            self = self.rest
        while other is not Link.empty:
            ret = Link(other.first, ret)
            other = other.rest
        return reverse(ret)




# Question Two
def insert(link, value, index):
    """Inserts value into Link at given index."""
    if index >= len(link):
        return "Index out of bounds."
    else:
        if index == 0:
            link.rest = Link(link.first, link.rest)
            link.first = value
        else:
            return insert(link.rest, value, index - 1)


# Question Four
def link_to_list(link):
    """Takes Link and returns a list with the same elements."""
    lst = []
    while link is not Link.empty:
        lst.append(link.first)
        link = link.rest
    return lst


# Question Five
def reverse(link):
    """Returns a reversed Link."""
    new = Link(link.first)
    while link.rest is not Link.empty:
        link = link.rest
        new = Link(link.first, new)
    return new
