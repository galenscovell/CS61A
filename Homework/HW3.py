
# Question One
# G(n) = n,                                       if n <= 3
# G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
def g(n):
    """Return value of G(n), computed recursively."""
    if n <= 3:
        return n
    else:
        return g(n - 1) + (2 * g(n - 2)) + (3 * g(n - 3))

def g_iter(n):
    """Return value of G(n), computed iteratively."""
    if n <= 3:
        return n
    total = 0
    results = [0, 1, 2, 3]
    for x in range(4, n + 1):
        m1, m2, m3 = x - 1, x - 2, x - 3
        if m3 > 3:
            total = results[m1] + (2 * results[m2]) + (3 * results[m3])
        elif m2 > 3:
            total = results[m1] + (2 * results[m2]) + (3 * m3)
        elif m1 > 3:
            total = results[m1] + (2 * m2) + (3 * m3)
        else:
            total = m1 + (2 * m2) + (3 * m3)
        results.append(total)
    return results[-1]



# Question Two
def has_seven(k):
    """
    Returns True if at least one digit of k is a 7.
    Do not use any assignment statements, only recursion.
    """
    if k < 10:
        if k == 7:
            return True
        else:
            return False
    return has_seven(k % 10) or has_seven(k // 10)
    


# Question Three
def pingpong(n):
    """
    Return nth element of ping-pong sequence.
    No assignment statements; however, you may use def statements.

    The ping-pong sequence counts up starting from 1 
    and is always either counting up or counting down. 

    At element k, the direction switches if k is a multiple of 7
    or contains the digit 7.
    """
    def check(k):
        if k < 7:
            return 1
        if k % 7 == 0 or has_seven(k):
            return check(k - 1) + 1
        return check(k - 1)

    if n <= 7:
        return n
    if check(n - 1) % 2 == 0:
        return pingpong(n - 1) - 1
    return pingpong(n - 1) + 1



# Question Four
def count_change(amount):
    """Return the number of ways to make change for amount."""
    def check_pow(num):
        return num == 1 or (num & (num - 1)) == 0

    def create_coins():
        possible_coins = []
        for coin in range(1, amount + 1):
            if check_pow(coin):
                possible_coins.append(coin)
        return count(possible_coins)

    def count(coins):
        ways = [1] + [0] * amount
        for coin in coins:
            for k in range(coin, amount + 1):
                ways[k] += ways[k - coin]
        return ways[amount]

    return create_coins()



# Question Five
def hanoi(n, start, end):
    """
    Print the moves required to solve the towers of hanoi game, 
    starting with n disks on the start pole and finishing on the end pole.

    The game is assumed to have 3 poles.
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"

    print(n, start, end)
    if n > 0:
        hanoi(n - 1, start, 6 - start - end)
        print('Move disk %d, rod %d -> rod %d' % (n, start, end))
        hanoi(n - 1, 6 - start - end, end)