
# Interfaces are shared sets of attributes with specified behavior.
# Other programs don't need to know how each data type implements
# the interface, only that they have implemented it.

# Interfaces can be implemented by user-defined classes
# Methods such as __getitem__ are polymorphic functions, a type of 
#   generic function

from math import sqrt
class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __getitem__(self, n):
        """Sequence interface.
        >>> vector1[2]
        3
        """
        return self.vector[n]

    def __len__(self):
        """Sequence interface.
        >>> len(vector1)
        4
        """
        return len(self.vector)

    def __neg__(self):
        """Arithmetic interface.
        >>> -vector1
        [-1, -2, -3, -4]
        """
        return [-x for x in self.vector]

    def __add__(self, other):
        """Arithmetic interface.
        >>> vector1 + vector2
        [5, 5, 5, 5]
        """
        return [x + y for x, y in zip(self.vector, other.vector)]

    def __mul__(self, other):
        """Arithmetic interface.
        >>> vector1 * 5
        [5, 10, 15, 20]
        >>> vector1 * vector2
        [4, 6, 6, 4]
        """
        if type(other) in (int, float):
            return [x * other for x in self.vector]
        elif type(other) is Vector:
            return [x * y for x, y in zip(self.vector, other.vector)]

vector1 = Vector([1, 2, 3, 4])
vector2 = Vector([4, 3, 2, 1])