
# Generic functions are functions that are able to work on a variety
# of different objects by analyzing what type they are and calling
# the proper method depending on found type.

# Type Dispatching: Provide different methods in generics for
# dealing with different types.

# Type Coercion: Convert types to other types in order to allow
# generic functionality.

# This is an implementation creating rational and complex numbers
# and being able to add or multiple them in whichever combination.


from fractions import gcd


def add_complex_and_rational(c, r):
    return ComplexRI(c,real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)

def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)

class Number:
    """Numbers that can be combined using type dispatching.

    >>> ComplexRI(1.5, 0) + Rational(3, 2)
    ComplexRI(3, 0)
    >>> Rational(-1, 2) * ComplexMA(4, pi/2)
    ComplexMA(2, 1.5 * pi)
    """

    def __add__(self, other):
        """ '+' operations use this special method."""
        # If types are same, use default operation
        if self.type_tag == other.type_tag: 
            return self.add(other)
        # Otherwise look up defined method
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    def __mul__(self, other):
        """ '*' operations use this special method."""
        if self.type_tag == other.type_tag: 
            return self.mul(other)
        # Otherwise look up defined method
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    adders = { ('com', 'rat'): add_complex_and_rational,
              ('rat', 'com'): add_rational_and_complex }

    multipliers = { ('com', 'rat'): mul_complex_and_rational,
              ('rat', 'com'): mul_rational_and_complex }


# Rational numbers
class Rational(Number):
    """A rational number represented as a numerator and denominator."""
    type_tag = 'rat'

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)

    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)





# Complex numbers
class Complex(Number):
    type_tag = 'com'

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)


class ComplexRI(Complex):
    """A rectangular representation."""
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.image ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)
    

class ComplexMA(Complex):
    """A polar representation."""
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)