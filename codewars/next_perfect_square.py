"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

    examples:

    findNextSquare(121) --> returns 144
    findNextSquare(625) --> returns 676
    findNextSquare(114) --> returns -1 since 114 is not a perfect

    todo learn how to determine if a number is an integer w/o relying on built in functions/methods
"""

import math


def find_next_square(sq):

    sr = math.sqrt(sq)

    if not sr.is_integer():  # is_integer is apparently a method of floats, feels like cheating
        return -1

    return int(math.pow(sr + 1.0, 2))

l = [121, 625, 319225, 7]

for i in l:
    print(find_next_square(i))