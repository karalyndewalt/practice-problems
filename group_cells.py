
# Given an input array showing the positions of occupied cells,
# return a list of 'groups' where each group consists of a in_list
# of indices of connected cells.

"""

grid = [
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
]

groups = [
    [(0, 2), (0, 3), (1, 1), (1, 2), (1, 3)],
    [(3, 0), (3, 1)],
]

>>> get_groups(grid)
[[(0, 2), (0, 3), (1, 1), (1, 2), (1, 3)],[(3, 0), (3, 1)]]

"""

# valid connections - up, down, left, right
1. iterate over list until occupied cell found - add corrdinates to set
    2. from occupied cell, find all neighbors






def get_groups(grid):
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()
