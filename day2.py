import re

with open('day2_input_1.txt') as f:
    pws = f.readlines(
    )
valid = 0


def valid_1(pw):
    m = re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', pw)
    _min, _max, letter, _pass = m.groups()
    _min = int(_min)
    _max = int(_max)
    if _pass.count(letter) < _min or _pass.count(letter) > _max:
        return False
    else:
        return True

def valid_2(pw):
    m = re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', pw)
    first, second, letter, _pass = m.groups()
    first = int(first) - 1
    second = int(second) - 1
    return (_pass[first] == letter) != (_pass[second] == letter)

for pw in pws:
    if valid_2(pw):
        valid += 1

print(valid)
