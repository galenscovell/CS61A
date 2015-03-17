
# Iterator is a mutable object that can provide the next element of a sequence.
# 'iter' function creates iterator object by calling '__iter__' on argument.

# Built-in 'next' function invokes '__next__' method on its argument to
# provide the next element of the iterator sequence.

# If there is no next element of iterator, StopIteration exception is raised.

class RangeIter:
    """Remake built-in iter(range()) object."""
    def __init__(self, start, end):
        self.next = start
        self.end = end

    def __next__(self):
        if self.next >= self.end:
            raise StopIteration
        result = self.next
        self.next += 1
        return result


x = range(-2, 2)
xi = iter(x)
yi = RangeIter(-2, 2)



# Iterable represents a sequence and returns a new iterator on __iter__
# Dictionaries, lists, sequences, etc. are iterable

class LetterIter:
    """
    >>> a_to_e = LetterIter('a', 'e')
    >>> next(a_to_e)
    'a'
    >>> next(a_to_e)
    'b'
    """
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration
        result = self.next_letter
        self.next_letter = chr(ord(result) + 1)
        return result

class Letters:
    """
    >>> s = Letters('a', 'e')
    >>> si = iter(s)
    >>> next(si)
    'a'
    >>> next(si)
    'b'
    """
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end

    def __iter__(self):
        return LetterIter(self.start, self.end)



# Python makes heavy use of iterators!
# Some built-in iterators:
"""
map(func, iterable)          : Iterate over func(x) for x in iterable
filter(func, iterable)       : Iterate over x in iterable if func(x)
zip(first_iter, second_iter) : Iterate over co-indexed (x, y) pairs
reversed(sequence)           : Iterate over x in a sequence in reverse order

list(iterable)   : Create a list containing all x in iterable
tuple(iterable)  : Create a tuple containing all x in iterable
sorted(iterable) : Create a sorted list containing x in iterable

    When executing a for statement:
        __iter__ returns an interator and
        __next__ provides each item
"""