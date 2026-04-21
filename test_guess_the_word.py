# Chris Rogers
# CIS256 Spring 2026
# Exercise Assignment 4

import random

# Import function from our game file
from guess_the_word import get_word, words


def tests():

    # Test 1 checking for proper display of correctly
    # guessed letters.
    result = get_word("pasta", ["p"])
    if result == "p _ _ _ _":
        print("Letters are showing as expected.")
    else:
        print("Test failed.")

    #Test 2 checking for not showing incorrect letters.
    result = get_word("pasta", ["q"])
    if result == "_ _ _ _ _":
        print("Wrong answers do not show up in result.")
    else:
        print("Test failed.")

    # Test 3 checks that words from the list are selected.
    word = random.choice(words)
    if word in words:
        print(f"'{word}' does show up in the game list.")
    else:
        print("Test Failed.")

tests()