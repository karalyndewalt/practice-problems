# Given a list of numbers combine them to make the largest numberself.

# 1. transform all numbers to strings
# 2. iterate over list with while loop
# 3. compare 0th index to right neighbor,
#     4. if smaller, move right
#     5. if == compare next index
#         6. if no next index, stay
# 7. join list to make one big string
# 8. return string as number


def gen_longest_num(nums):
    """ Returns largest combination of numbers from list

    >>> gen_longest_num([1,2,3])
    321

    >>> gen_longest_num([3, 30, 34, 5, 9])
    9534330

    >>> gen_longest_num([54, 546, 548, 60])
    6054854654
    """

    str_nums = [str(x) for x in nums]

    rotated = True

    while rotated:

        rotated = False
        # print range(len(nums)-1)

        for i in range(len(str_nums)-1):
            current = str_nums[i]
            neighbor = str_nums[i+1]

            if (neighbor + current) > (current + neighbor):
                str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                rotated = True

    # str_nums = [str(x) for x in nums]
    result = "".join(str_nums)
    return int(result)
            # if current[0] == neighbor[0]:
            #     longer = ""
            #     if len(current) > len(neighbor):
            #         longer = current
            #     else:
            #         longer = neighbor
            #
            #     # evaluate the next number
            #     for k in range(1, len(longer) +1):
            #         try:
            #             if current[k] < neighbor[k]:
            #                     str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
            #         except IndexError:
            #             if neighbor



                    # do some iterative comparison

            # elif current[0] < neighbor[0]:
            #
            #     str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                # rotated = True


        # rotated = False






if __name__ == "__main__":
    import doctest
    doctest.testmod()
