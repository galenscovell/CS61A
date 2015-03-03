
# Property methods allow value of instance attributes to stay in sync

# @property decorator on method designates that it will be called
# whenever it is looked up on an instance


class Rational:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    @property
    def float_value(self):
        return self.numer / self.denom