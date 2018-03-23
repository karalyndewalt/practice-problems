
Power Set
=========

Write a program that generates the power set from a set of numbers.

Example:
powerSet([‘a’, ‘b’, ‘c’])

Solution: [[], ["a"], ["b"], ["a", "b"], ["c"], (["a", "c"]), ["b", "c"], ["a", "b", "c"]]



def make_power_set(org_set):
    """ Return list of all subsets of the original

    >>> make_power_set([‘a’, ‘b’, ‘c’])
    set([[], ["a"], ["b"], ["a", "b"], ["c"], ["a", "c"], ["b", "c"], ["a", "b", "c"]])

    """

    result = []

    if len(org_set) > 0:

        for i in range(len(org_set)):
            make_power_set(org_set[])
