
# String representation

# repr() => Python interpreter format
#  str() => Human-readable format
import datetime

today = datetime.date(2015, 3, 1)
"""
>>> repr(today)
'datetime.date(2015, 3, 1)'
>>> str(today)
'2015-03-01'
>>> eval(repr(today))
datetime.date(2015, 3, 1)
"""

# Polymorphic functions: functions tht apply to main different forms of data
# str() and repr() are polymorphic

class Bear:
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear instance'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    """
    >>> print_bear()
    a bear
    Bear()
    a bear
    oski
    this bear instance
    """
    oski = Bear()
    print(oski)
    print(repr(oski)) # goes straight to class
    print(str(oski))
    print(oski.__repr__()) # looks up instance method first
    print(oski.__str__()) # looks up instance method first

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)