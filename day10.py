from collections import defaultdict
from functools import reduce
from itertools import combinations

with open('day10_input.txt') as f:
    all_adapters = [int(l.strip()) for l in f.readlines() if l.strip()]

def chain(adapters):
    adapters.sort()
    gaps = defaultdict(int)
    cur = adapters[0]
    for a in adapters[1:]:
        gaps[a-cur] += 1
        cur = a
    return gaps

def chop_into_separate_parts(adapters):
    parts = []
    prev = adapters[0]
    cur_part = []
    for a in adapters:
        if a - prev == 3:
            parts.append(cur_part)
            cur_part = []
        cur_part.append(a)
        prev = a
    parts.append(cur_part)
    return parts

def arrangements_of(adapters):
    '''
    so the idea is to do the expensive calculation only on small groups of
    adapters that have guaranteed endpoints

    then since the gaps can't like overlap or whatever you can multiple the possible
    arrangements in each chunk together

    this only works if the 3-jolt gaps are reasonably friendly in their placement
    but they are in my actual input
    which does not feel
    like a
    coincidence

    the fully general solution seems way harder? like, if the input were just the numbers
    1-100, this would completely fail.

    ok i looked it up it's actually pretty easy, i'm just stupid
    you just like... go through the list of adapters and calculate how many ways
    you can get to each adapter, and then add the next one. straightforward DP solution
    that i'm too dumb to figure out on my own. oh well.
    '''
    if len(adapters) < 3:
        return [adapters]

    # stupidest possible thing
    def is_valid(arrangement):
        start = arrangement[0]
        for a in arrangement[1:]:
            if a - start > 3:
                return False
            start = a
        return True
    total = 1
    valid = [adapters]
    removable_indices = list(range(1, len(adapters) - 1))
    for i in range(len(removable_indices)):
        combs = combinations(removable_indices, i+1)
        for c in combs:
            without = [
                adapters[j] for j in range(len(adapters))
                if j not in c
            ]
            if is_valid(without):
                total += 1
                valid.append(without)
    #print(valid)
    return valid

def splice(a, start, num):
    return a[:start] + a[start+num:]

assert len(all_adapters) == len(set(all_adapters))
adapters_with_endpoints = all_adapters + [0, max(all_adapters) + 3]
gaps = chain(adapters_with_endpoints)

parts = chop_into_separate_parts(adapters_with_endpoints)
s = reduce(lambda a, b: a + b, parts, [])
assert adapters_with_endpoints == s

acc = 1
for p in parts:
    arrs = arrangements_of(p)
    acc *= len(arrs)
    print(arrs)
print(acc)

'''
0, 1, 2, 3, 4
0,    2, 3, 4
0, 1,    3, 4
0, 1, 2,    4
0,       3, 4
0,    2,    4
0, 1,       4
 '''