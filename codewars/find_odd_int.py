"""
from codewars.com

return the integer that occurs and odd # of times in a list, given
that only one integer in the list will occur an odd # of times
"""

l1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
l2 = [10]
l3 = [1,1,1,1,1,1,10,1,1,1,1]  # the correct value occurs only once
l4 = [1,1,1,1,1,1,10,1,1,1,1,10]  # none occur an odd # times

ll = [l1, l2, l3, l4]


def find_it(seq):
    if len(seq) == 1:
        return seq[0], 1

    seq.sort()

    # candidate is the value in the list we're currently testing to determine if it occurs
    # an odd # of times

    candidate = seq.pop(0)
    value_count = 1

    for v in seq:

        # this is a new value, different from the current candidate value, it might become a new candidate
        if v != candidate:

            if value_count % 2 == 1:  # did current candidate occur an odd # of times

                return candidate, value_count

            # current candidate occurred an even # of times, so we don't care about it any longer
            # make the current value from the list the new current candidate and re-init it's count to 1
            else:
                candidate = v
                value_count = 1

        else:  # the current list value is same as the current candidate value
            value_count += 1

    # this last set of checks is required for the corner case of the last
    # value in the sorted list being the one that occurs an odd # of times
    # which requires that it occur only once.  In that case, it will "fall
    # out" of the for loop, so check value_count one last time, if it's odd
    # then this corner case occurred, otherwise, return None, None
    if value_count % 2 == 1:
        return candidate, value_count
    else:
        return None, None


for l in ll:

    r = find_it(l.copy())

    if r == (-1, -1):
        print('Hit the final return')
    else:
        print(r)


#### alternative solutions (from codewars) ####

def findit_2(l):

    for v in l:
        if l.count(v) % 2 == 1:  # just keep recounting the #'s, which is probably faster (check?)
            return v
    return None


print('find2')

for l in ll:
    print(findit_2(l.copy()))

######################


import operator


def findit_3(xs):
    return reduce(operator.xor, xs)