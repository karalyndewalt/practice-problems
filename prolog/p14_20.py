def duplicate_lst(lst):
    """ Returns new list, duplicating each element of the list

    >>> duplicate_lst([1,2,3])
    [1, 1, 2, 2, 3, 3]

    """

    out = []
    for x in lst:
        out.extend((x, x))

    return out

# return [x for x in lst for i in (1,2)]


def duplicate_by(lst, multi):
    """Returns new lits, duplicating each element by multi var

    >>> duplicate_by([1,2,3], 3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]

    """
    # out = []

    # for x in lst:
    #     out.extend([x for i in xrange(multi)])
    # return out
    return [x for x in lst for i in xrange(multi)]


def drop_nth(lst, n):
    """ Return new list, dropping each Nth element

    >>> drop_nth([1,2,3,4,5,6,7,8,9,10], 2)
    [1, 3, 5, 7, 9]

    >>> drop_nth([1,2,3,4,5,6,7,8,9,10], 3)
    [1, 2, 4, 5, 7, 8, 10]
    """
    return [lst[idx] for idx in xrange(len(lst)) if (idx+1) % n]
    # return lst[::n]


def split_list(lst, length):
    """Return list split in two, given length of the first list

    >>> split_list([1,2,3,4,5,6,7,8,9,10], 2)
    ([1, 2], [3, 4, 5, 6, 7, 8, 9, 10])
    """


    return (lst[:length], lst[length:])


def get_slice(lst, start, end):
    """ Return slice from start to end, inclusive

    >>> get_slice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"], 2, 7)
    ['c', 'd', 'e', 'f', 'g', 'h']

    """

    return lst[start: (end + 1)]


# def 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
