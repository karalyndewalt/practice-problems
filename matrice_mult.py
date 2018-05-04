A = [
    [5, 6],
    [8, 9]
    ]


B = [
    [1, 2],
    [4, 5]
    ]


def multiply_matrix(mat_a, mat_b):
    """Returns multiplcation of matrix

    >>> multiply_matrix(A, B)
    [[29, 40], [44, 61]]

    """

    size_a = len(mat_a[0])
    size_b = len(mat_b)


    if size_a != size_b:
        print "Cannot multipy unmatched size matrices"
        return None
    rng_a = range(size_a)

    result = [[0 for col in rng_a] for row in rng_a]

    for i in rng_a:
        for j in rng_a:
            for k in rng_a:
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    return result

C = multiply_matrix(A, B)
