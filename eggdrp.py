def my_function(arg):
    # write the body of your function here
    return 'running with %s' % arg

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function('test input')


def egg_drop(break_floor):

    top = 100
    floors_to_jump = 14
    current_floor = 14
    num_drops = 1

    def egg_drop_test():

        while current_floor < break_floor:
            current_floor += floors_to_jump
            floors_to_jump -= 1
            num_drops += 1
            egg_drop_test()

        # we have exceded break_floor - move iteratively from last known break-free
        # floor
        floors_to_jump = 1
        if num drops == 1:
            current_floor = 1

            while current_floor < break_floor:
                current_floor += floors_to_jump
                num_drops += 1
                egg_drop_test()

        return (current_floor, num_drops)







print egg_drop_test(14)
print egg_drop_test(28)
