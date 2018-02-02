def fizz_buzz(lst):
    """reads each number in a list, printing
    'fizz' if divisable by 3,
    'buzz' if divisable by 5,
    'fizzbuzz' if divisable by both 3 and 5
    """
    for num in lst:
        if num % 3 == 0 and num % 5 == 0:
            print "fizzbuzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print "a very boring number "
