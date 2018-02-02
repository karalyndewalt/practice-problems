"""Given an infinite supply of dimes and pennies, find the different amounts of
money that can be created with exactly `num_coins` coins.
For example, when num_coins = 3, you can create:
    3 = penny + penny + penny
    12 = dime + penny + penny
    21 = dime + dime + penny
    30 = dime + dime + dime
For example:
"""


def coin_values(num_coins):
    """
    >>> coin_values(0)
    set([0])
    >>> coin_values(1)
    set([1, 10])
    >>> coin_values(2)
    set([2, 11, 20])
    >>> coin_values(3)
    set([3, 12, 21, 30])
    >>> coin_values(11)
    set([65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29])
    """


    # purse = [1 for x in range(nums)]
    values = [num_coins]

    for i in range(num_coins):
        values.append((values[-1]) + 9)

    # print values
    return set(values)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
