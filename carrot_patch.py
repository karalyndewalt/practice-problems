

"""Traverse the Matrix to largest carrot sum

This will be a greedy solution/algorithim, choose the largest value available at each
step.

begin at center, or largest value of 'center'
remove (eat) all carrots from location (replace with zero)
don't need diagonal moves u,d,l,r only
sleep when no adjacent squares have carrots. (also edges)

carrot_patch = [[5, 7, 8, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 4, 9],
                [3, 1, 0, 5, 8],
                [3, 1, 0, 5, 8]]

marlon_bundo_eat(carrot_patch)
30
"""


def on_board(pos, size):
    """Checks if a coodinate set is on a board of size

    'size' is a tuple of the form (height, width)

    """

    row, col = pos
    height, width = size

    return 0 <= row <= width and 0 <= col <= height


def get_carrot_count(matrix, pos, size):
    """Returns (count, (row, col)), if on board. Else - (0, (-1, -1))"""

    row, col = pos

    if on_board(pos, size):
        return (matrix[row][col], pos)

    return (0, (-1, -1))


def eat_max_carrots(matrix, pos, total=None):
    """Returns total carrots consumed following greedy path beginning at 'pos'
    """

    height = len(matrix) #rows
    width = len(matrix[0]) #columns

    row, col = pos
    # get first carrot crop and clear val in matrix
    if total is None:
        total = matrix[row][col]
        matrix[row][col] = 0

    # look up and down, left and right
    udlr = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    neighbors = [get_carrot_count(matrix, x, (height, width)) for x in udlr]

    biggest_neighbor = max(neighbors)
    # print biggest_neighbor
    # have we run out of spaces/carrots?
    if biggest_neighbor[0] == 0:
        return total
    new_pos = biggest_neighbor[1]

    new_row, new_col = new_pos
    matrix[new_row][new_col] = 0
    return eat_max_carrots(matrix, new_pos, (total + biggest_neighbor[0]))


def get_center(num):
    """Returns list of center points for list"""

    half = num/2

    center = []

    # is even (half-1, half)
    if num % 2 == 0:
        center.extend([half - 1, half])
    # is odd half (use floor)
    else:
        center.append(half)

    return center


def find_center_coordinate(matrix):
    """Returns coordinates for center of n x m matrix

        Odd board returns center coordinates
        Even board returns coordinates of highest value found in center group.

    """

    height = len(matrix)
    width = len(matrix[0])
    size = (height, width)

    row_centers = get_center(height)
    col_centers = get_center(width)

    coordinate_set = [(row, col) for row in row_centers for col in col_centers]
    coordinates = max([get_carrot_count(matrix, pos, size,) for pos in coordinate_set])

    return coordinates[1]


def marlon_bundo_eat(matrix):
    """Returns sum of highest value traversal from the matrix center

    Uses center or highest value from center group
    """

    # num_rows = len(matrix)
    # num_columns = len(matrix[0])
    #
    # # if both the rows and columns are odd you have a center pt. at the floor
    # # division of both the column and rows.
    #
    # row_mid_pt = num_rows/2
    # col_mid_pt = num_columns/2
    #
    # # for now (time constraints) assume center for odd, regular matrix
    # center = (row_mid_pt, col_mid_pt)

    center = find_center_coordinate(matrix)
    print center

    total = eat_max_carrots(matrix, center)

    return total


carrot_patch = [[5, 7, 8, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 4, 9],
                [3, 1, 0, 5, 8],
                [3, 1, 0, 5, 8]]

print find_center_coordinate(carrot_patch)

total_carrots = marlon_bundo_eat(carrot_patch)

print total_carrots
