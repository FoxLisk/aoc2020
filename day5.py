import math

def parse_seat(seat):
    min = 0
    max = 127
    for i in range(7):
        if seat[i] == 'F':
            max = math.floor((min + max) / 2)
        elif seat[i] == 'B':
            min = math.ceil((min + max) / 2)
        else:
            raise ValueError('bad parse: %r' % seat)
    assert max == min
    minc = 0
    maxc = 7
    for i in range (3):
        c = seat[i + 7]
        if c == 'L':
            maxc = math.floor((minc + maxc) / 2)
        elif c == 'R':
            minc = math.ceil((minc + maxc) / 2)
        else:
            raise ValueError('bad column parse: %r' % seat)
    return min, minc

ids = []
with open('day5_input.txt') as f:
    for line in f.readlines():
        row, col = parse_seat(line)
        id = (row*8) + col
        ids.append(id)

ids.sort()

has_prev = False
last_id = None
for i in range(len(ids) - 1):
    if ids[i] + 2 == ids[i+1]:
        print(ids[i] + 1)

