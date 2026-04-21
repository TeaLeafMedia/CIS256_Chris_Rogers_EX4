# Chris Rogers
# CIS256 Spring 2026
# Exercise Assignment 4

# Import function from our game file
from guess_the_word import get_word


# Test 1 checking for proper display of correctly
# guessed letters.
def tests():
    result = get_word("pasta", ["p"])
    if result == "p _ _ _ _":
        print("Letters are showing as expected.")
    else:
        print("Test failed.")