"""
Check to see if a string has the same amount of 'x's and 'o's. The method
must return a boolean and be case insensitive. The string can contain any char.

my assumptions:
    * there is at least one x or o in the string
"""

s = 'xooabcZ'


def xo(s):

    s = s.lower()
    s = sorted(s)  # probably not required

    return s.count('x') == s.count('o')  # if the counts are same returns True, False otherwise


print(xo(s))