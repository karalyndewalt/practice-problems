"""Problems from Prolog Site solved in python"""

# def get_last(lst):
#     """Returns last item from a list
#     >>> get_last([1])
#     1
#     >>> get_last(['a', 'b', 'c'])
#     'c'
#     >>> get_last([1, 2, 3, 4, 5, 6])
#     6
#     """
#
#     # could just use pythonism lst[-1]
#     return lst[(len(lst) - 1)]
#
# def is_palindrome(lst):
#     """Returns True if list is a palindrome
#     >>> is_palindrome([1, 2, 1])
#     True
#     >>> is_palindrome([1,1])
#     True
#     >>> is_palindrome([1,2])
#     False
#     """
#
#     if len(lst) < 2:
#         return True
#
#     if lst[0] != lst[-1]:
#         return False
#
#     return is_palindrome(lst[1: -1])

#
# def flatten(nested):
#     """
#     Return single list of elements from nested structure
#
#     >>> flatten([[1]])
#     [1]
#     >>> flatten([[1], [1]])
#     [1, 1]
#     >>> flatten([[1, [2]]])
#     [1, 2]
#     >>> flatten([[[3, 4]]])
#     [3, 4]
#     >>> flatten(['a', ['b', ['c', 'd'], 'e']])
#     ['a', 'b', 'c', 'd', 'e']
#     """
#
#     flat_lst = []
#     # print nested
#     for item in nested:
#         if isinstance(item, list):
#             flat_lst += flatten(item)
#         else:
#             flat_lst.append(item)
#     return flat_lst
#
#
# def compress(lst):
#     """
#     Returns list of items with local duplicates removed
#
#     >>> compress([1,1,1,2,3])
#     [1, 2, 3]
#     >>> compress([1,2,2,2,3])
#     [1, 2, 3]
#     >>> compress([1,2,2,2,3,2])
#     [1, 2, 3, 2]
#     """
#
#     stack = lst
#
#     for num in range((len(stack) - 1), -1, -1):
#         if lst[num] == lst[num - 1]:
#             stack.pop(num)
#
#     return stack
#
#
# def pack(lst):
#     """Returns list of duplicates captured in sub lists
#     >>> pack([1,1,1,2,3])
#     [[1, 1, 1], [2], [3]]
#     >>> pack([1,1,2,2,2,3,3])
#     [[1, 1], [2, 2, 2], [3, 3]]
#     """
#     from itertools import groupby
#
#     return [list(group) for key, group in groupby(lst)]
#
#     # result = [[lst[0]]]
#     #
#     # for i in lst[1:]:
#     #     if i in result[-1]:
#     #         result[-1].append(i)
#     #     else:
#     #         result.append([i])
#     #
#     # return result


def compress_encode(lst):
    """
    Returns enumerated list of lists,
    consecutive duplicates only compressed.
    >>> compress_encode([1,1,1,2,3])
    [[3, 1], [1, 2], [1, 3]]
    >>> compress_encode([1,1,2,2,2,3,3])
    [[2, 1], [3, 2], [2, 3]]
    """

    from itertools import groupby

    return [[len(list(group)), key] for key, group in groupby(lst)]

    # result = [[1, lst[0]]]
    #
    # for i in lst[1:]:
    #     if i == result[-1][1]:
    #         result[-1][0] += 1
    #     else:
    #         result.append([1, i])
    #
    # return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print compress_encode([1, 1, 1, 2, 3])
