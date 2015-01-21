
# Question One
def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the third is not."""
    def equal(x, y):
        return x == y
    x = 0
    if equal(a, b):
        x += 1
    if equal(b, c):
        x += 1
    if equal(a, c):
        x += 1
    return x == 1


# Question Two
def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone sequence."""
    def hailstone(n, m):
        if n == m:
            return True
        else:
            if n == 1:
                pass
            elif n % 2 == 0:
                return hailstone(n // 2, m)
            else:
                return hailstone(3 * n + 1, m)
    if hailstone(a, b):
        return True
    elif hailstone(b, a):
        return True
    else:
        return False


# Question Three
def near_golden(perimeter):
    """Return the integer height of near-golden rectangle with PERIMETER. 
    (Dictionaries haven't been introduced in the course yet, but this seems like the best method)"""
    ratios = {}
    for w in range(2, perimeter):
        for h in range(2, perimeter):
            if w > h and ((2 * w) + (2 * h)) == perimeter:
                r1, r2 = h / w, (w / h) - 1
                new = abs(r2 - r1)
                ratios[w, h] = new

    min_ratio = min(ratios, key=ratios.get)
    return min_ratio[1]

                