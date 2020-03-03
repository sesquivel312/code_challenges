"""
You live in the city of Cartesia where all roads are laid
out in a perfect grid. You arrived ten minutes too early to
an appointment, so you decided to take the opportunity to
go for a short walk. The city provides its citizens with a
Walk Generating App on their phones -- everytime you press
the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block in a direction and you
know it takes you one minute to traverse one city block, so
create a function that will return true if the walk the app
gives you will take you exactly ten minutes (you don't want
to be early or late!) and will, of course, return you to
your starting point. Return false otherwise.

test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');

I think the answer is:
    1. array must be len 10
    2. assign directions to X, Y axes, each one adds/subtracts one from the original
       position - call that 0,0 - the result must still be 0,0

       nb: n = (0,+1), w= (-1,0)
"""


def is_valid_walk(walk):
    """
    walk is a list of directions, n, s, e, w

    :param walk:
    :return:
    """

    if not len(walk) == 10:
        return False

    n = walk.count('n')
    s = walk.count('s')
    e = walk.count('e')
    w = walk.count('w')

    if n - s == 0 and e - w == 0:
        return True
    else:
        return False


def is_valid_walk2(w):

    # more concise alternative
    return len(w) == 10 and w.count('n') == w.count('s') and w.count('e') == w.count('w')


w1 = ['n','s','n','s','n','s','n','s','n','s']  # true
w2 = ['w','e','w','e','w','e','w','e','w','e','w','e']  # false
w3 = ['w']  # false
w4 = ['n','n','n','s','n','s','n','s','n','s']  # false

walks = [w1, w2, w3, w4]

for w in walks:
    print(is_valid_walk(w))

for w in walks:
    print(is_valid_walk2(w))


