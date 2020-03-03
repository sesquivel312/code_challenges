"""
The Western Suburbs Croquet Club has two categories of membership,
Senior and Open. They would like your help with an application form
that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a
handicap greater than 7. In this croquet club, handicaps range from
-2 to +26; the better the player the lower the handicap.
Input

Input will consist of a list of lists containing two items each. Each
list contains information for a single potential member. Information
consists of an integer for the person's age and an integer for the
person's handicap.

Example Input: [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

Ex. output: ["Open", "Open", "Senior", "Open", "Open", "Senior"]

"""

def open_or_senior(members):

    cat = []

    for m in members:
        if m[0] > 54 and m[1] > 7:
            cat.append('Senior')
        else:
            cat.append('Open')

    return cat

def open_or_senior2(members):

    return ['Senior' if a > 54 and h > 7 else 'Open' for a, h in members]


m1 = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

mm = [m1, ]

for m in mm:

    print(open_or_senior2(m))