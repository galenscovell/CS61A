
# Creates pair without the use of built-in list datatype

def pair(x, y):
    """Return pair containing x and y."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return ith element of pair p."""
    return p(i)

point = pair(3, 4)
select(point, 1)