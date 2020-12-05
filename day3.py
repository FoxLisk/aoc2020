map = []
with open('day3_input_1.txt') as f:
    for line in f.readlines():
        map.append(line.strip())
width = len(map[0])


def handle_slope(dx, dy, do_print=False):
    hits = 0
    posx, posy = 0, 0
    pretty = []
    while posy < len(map):
        row = list(map[posy])
        if map[posy][posx] == '#':
            hits += 1
            row[posx] = 'X'
        else:
            row[posx] = 'O'
        if do_print:
            print(''.join(  row))
        posx = (posx + dx) % width
        posy += dy
    return hits

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    ( 1, 2)
]
cum = 1
for (dx, dy) in slopes:
    cum *= handle_slope(dx, dy)

print(cum)
