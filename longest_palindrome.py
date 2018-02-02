# Prompt: given a string, return the longest palindrome in that string.
# Examples:
    # embeded: 'abcdtacocatefg' -> 'tacocat'
    # full string: 'anna' -> 'anna'
    # no palindrome: 'ally' -> ''
    # mulitiple palindromes: 'abbabobtacocat' -> 'tacocat'

# 1. Write a function to identify stand-alone palindromes.
#     a. iterate over string
#     b. compare first and last char, (if mis-match bail. if matching, continue.)
#     c. return T/F
#
# 2. Approach from the 'top down'. Start with the whole word to see if it is a
# palindrome.
# 3. If it is not a palindrome, move from right to left and check again.
# 4. When you find a palindrome, compare it to what you have already seen.
#     a. begin with an empty string
#     b. replace if bigger, otherwise move onself.


# later optimizations will be to check if the remaining number of chars at each
# iteration is smaller than the largest seem palindrome, bailing if so.

def is_palindrome(word):
    """Returns True if word is a palindrome

    >>> is_palindrome("anna")
    True

    >>> is_palindrome("tacocat")
    True

    >>> is_palindrome("ally")
    False
    """

    for i in range(len(word)/2):
        # need to subtract one because indexing starts at 0.
        # without (i, -i) --> (0,0)
        if word[i] != word[(-i) - 1]:
            return False
    # made it through the whole word with out returning False, must be True
    return True


def find_longest_palindrome(word):
    """Returns longest palindrome in a string

    >>> find_longest_palindrome('abcdtacocatefg')
    'tacocat'

    >>> find_longest_palindrome('anna')
    'anna'

    >>> find_longest_palindrome('abbabobtacocat')
    'tacocat'

    >>> find_longest_palindrome('Able was I ere I saw Elba')
    'able was i ere i saw elba'

    """
    longest_seen = ""
    word = word.lower()
    # j is currently the left most letter
    for j in range(len(word)):
        # k is currently the right most letter
        for k in range(len(word)-1, j, -1):
            if word[j] == word[k]:
                pot_pal = word[j:k+1]
                if is_palindrome(pot_pal):
                    # if it is a palindrome, check to see if it's longer
                    # than anything we've seen so far.
                    if len(pot_pal) > len(longest_seen):
                        longest_seen = pot_pal

    return longest_seen



if __name__ == "__main__":
    import doctest
    doctest.testmod()
