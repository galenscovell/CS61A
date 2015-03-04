

# Order of growth is a combination of time and space(memory)
"""
   n: size of the problem
R(n): measurement of some resource used(time or space)

    R(n) = O(f(n))      (O = big-theta)
    This means that there are positive constants k1 and k2 such that:
        k1 * f(n) <= R(n) <= k2 * f(n)
"""


# Properties
"""
 Constants: constant terms don't affect order of growth.
Logarithms: base of logarithm doesn't affect order of growth.
   Nesting: when inner process is repeated for each step of outer 
        process, multiple steps in outer and inner process for total steps.
"""


# Comparison
"""
   O(b**n): Exponential growth (incrementing n scales R(n) by factor)
   O(n**2): Quadratic growth   (incrementing n increases R(n) by n)
      O(n): Linear growth      (size of n directly dictates steps)
O(sqrt(n)): Square root growth (size of sqrt(n) dictates steps)
 O(log(n)): Logarithmic growth (doubling n only increments R(n))
      O(1): Constant time      (size of n doesn't matter)
"""




# Factors
def factors_slow(n):
    """Test each k from 1 through n.
    Time = O(n)
    Space = O(1)
    """
    total = 0
    for x in range(1, n + 1):
        if n % x == 0:
            total += 1
    return total


from math import sqrt
def factors_fast(n):
    """Test each k from 1 to sqrt(n). For every k, n/k is also factor.
    Time = O(sqrt(n))
    Space = O(1)
    """
    k, total = 1, 0
    while k < sqrt(n):
        if n % k == 0:
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total




# Exponentiation
def exp_slow(b, n):
    """
    Time = O(n)
    Space = O(n)
    """
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def square(x):
    return x * x

def exp_fast(b, n):
    """
    Time = O(log(n))
    Space = O(log(n))
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)


# Analyzing factors_fast
"""
To check lower bound (minimum resources used):
    Use k1 = 1 
    Check statements outside loops [4 or 5]
    Check statements within loops [3 or 4]
    Check statement iterations [between sqrt(n - 1) and sqrt(n)]
    Total number of statements executed = 
        at least [4 + 3(sqrt(n - 1))]

To check upper bound (maximum resources used):
    Check maximum statements executed [5 + 4sqrt(n)]
    Find maximum operations required per statement (p)
    Choose k2 = 5p and m = 25
"""