
# Attribute names starting with one underscore are not meant to be 
# referenced externally.
# "Don't reference this directly, it may change."

class FibIter:
    """Iterator over Fibonacci numbers.
    >>> fibs = FibIter()
    >>> [next(fibs) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    def __init__(self):
        self._next = 0
        self._addend = 1

    def __next__(self):
        result = self._next
        self._addend, self._next = self._next, self._addend + self._next
        return result



# Names bound in local frame are not accesible to other environments
# (unless the frame is extended)


# A Singleton class is a class that only ever has one instance.
# NoneType (class of None) is a singleton class (None is its only instance)