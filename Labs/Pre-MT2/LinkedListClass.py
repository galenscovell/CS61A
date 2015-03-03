
# Linked list class: pairs are two-attribute objects
# Methods are recursive

class Link:
    """Linked list data abstraction.

    >>> s = Link(3, Link(4, Link(5)))
    Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[0]
    3
    >>> 2[1]
    4
    """

    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        """Special method: element selection []."""
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        """Special method: built-in len() function."""
        return 1 + len(self.rest)

    def __repr__(self):
        """Modified repr for object representation."""
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link({0}{1})'.format(self.first, rest_repr)