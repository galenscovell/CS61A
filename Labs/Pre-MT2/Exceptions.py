

# Exceptions
"""
    ...are raised when errors occur
    ...are handled by program to prevent the interpeter from halting
    ...are objects and have classes/constructors
    ...enable non-local continuations of control
    ...handling tends to be slow

Unhandled exceptions halt execution and print a stack trace!
"""


# Raising Exceptions
"""
Assert statements raise AssertionError exception:

    assert <expression>, <string>

    These are designed to be used liberally.
    They can be disabled with the '-O' flag at runtime.


Raise statements also raise exceptions:
    
    raise <expression>

            raise TypeError('Bad argument.')

    TypeError, NameError, KeyError, RuntimeError
"""


# Handling Exceptions
"""
Try statements handle exceptions:

    try:
        <try suite>
    except <exception class> as <name>:
        <except suite>

            try:
                x = 1/0
            except ZeroDivisionError as e:
                print('Handling a', type(e))
                x = 0
"""
