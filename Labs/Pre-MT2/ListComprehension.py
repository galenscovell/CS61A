
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def dis_1a():
    return [i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0]

def dis_1b():
    return [(lambda j: j * j)(2  * i) for i in [5, -1, 3, -1, 3] if i > 2]

def dis_1c():
    return [[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]]

def dis_2(lst):
    return [x * lst.index(x) for x in lst if lst.index(x) % 2 == 0]