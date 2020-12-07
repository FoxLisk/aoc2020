import re
from collections import defaultdict


def parse_input(lines):
    all_colors = set()
    containments = {}
    for l in lines:
        l = l.strip()
        top, contained = l.split('bags contain')
        top = top.strip()
        contained_bags = contained.rstrip('.').split(',')
        containments[top] = set()
        for bag in contained_bags:
            bag = bag.strip()
            if bag == 'no other bags':
                continue
            num, color = re.match(r'(\d)+ ([\w ]+) bags?', bag).groups()
            all_colors.add(color)
            containments[top].add((int(num), color))
    return containments

def hits_gold(containments, color):
    contains = containments[color]
    for num, color in contains:
        if color == 'shiny gold':
            return True
        elif hits_gold(containments, color):
            return True
    return False

def shiny_search(containments):
    outers = set()
    for c in containments:
        if hits_gold(containments, c):
            outers.add(c)
    return outers


def holds_how_many(containments, start_color):
    tot = 0
    for num, color in containments[start_color]:
        tot += num + (num * holds_how_many(containments, color))
    return tot

example = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
containments = parse_input(example.splitlines())
print(holds_how_many(containments, 'shiny gold'))
print(shiny_search(containments))
with open('day7_input.txt') as f:
    containments = parse_input(f.readlines())
    winners = (shiny_search(containments))
    print(len(winners))

print( holds_how_many(containments, 'shiny gold'))