
# A stream is a linked list, but the rest of the list is computed on demand
# Uses lazy computation and functions interchangeably with linked lists
# Streams have explicit first element and implicit rest

class Stream:
    """Lazily computed linked list.
    >>> s = Stream(1, lambda: Stream(6-2, lambda: Stream(9)))
    >>> s.first
    1
    >>> s.rest.first
    4
    """
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()

    def __init__(self, first, compute_rest = lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return rest of stream, computing if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    



def integer_stream(first=1):
    def compute_rest():
        return integer_stream(first + 1)
    return Stream(first, compute_rest)

def square_stream(s):
    squared = s.first * s.first
    return Stream(squared, lambda: square_stream(s.rest))

def add_streams(s, t):
    added = s.first + t.first
    def compute_rest():
        return add_streams(s.rest, t.rest)
    return Stream(added, compute_rest)