
# Representation of sequential data that does not explicitly store each element.

class Range:
    """Remaking the built-in Range class."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0, self.end - self.start)

    def __getitem__(self, k):
        if k < 0:
            k = len(self) + k
        if k < 0 or k >= len(self):
            raise IndexError
        return self.start + k

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start, self.end)

x = range(-2, 2)
y = Range(-2, 2)