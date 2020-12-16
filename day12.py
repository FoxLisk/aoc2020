import math

def get_raw_input():
    with open('day12_input.txt') as f:
        return f.read()

def get_input(raw):
    instrs = []
    for l in raw.splitlines():
        l = l.strip()
        if not l:
            continue
        instrs.append((l[0], int(l[1:])))
    return instrs

def run_p1(instrs):
    pos = [0, 0]
    dir = 0
    for t, val in instrs:
        if t in 'LR' and val != 90:
            print('Turn %r %r' % (t, val))
        if t == 'N':
            pos[1] += val
        elif t == 'W':
            pos[0] -= val
        elif t == 'E':
            pos[0] += val
        elif t == 'S':
            pos[1] -= val
        elif t == 'L':
            dir = (dir + val) % 360
        elif t == 'R':
            dir = (dir - val) % 360
        elif t == 'F':
            pos[0] += (math.cos(math.radians(dir))) * val
            pos[1] += (math.sin(math.radians(dir))) * val
        else:
            raise ValueError()
        print("After %r%r: %r (%r)" % (t, val, pos, dir))
    return pos


def run_p2(instrs):
    pos = [0, 0]
    wp = [10, 1]
    for t, val in instrs:
        if t in 'LR' and val != 90:
            print('Turn %r %r' % (t, val))
        if t == 'N':
            wp[1] += val
        elif t == 'W':
            wp[0] -= val
        elif t == 'E':
            wp[0] += val
        elif t == 'S':
            wp[1] -= val
        elif t in 'LR':
            if t == 'L':
                theta = math.radians(val)
            else:
                theta = math.radians(-val)
            # shamefully had to look these up T_T;;
            x = wp[0] * math.cos(theta) - wp[1] * math.sin(theta)
            y = wp[1] * math.cos(theta) + wp[0] * math.sin(theta)
            wp = [x, y]
        elif t == 'F':
            pos[0] += val*wp[0]
            pos[1] += val*wp[1]
        else:
            raise ValueError()
        print("After %r%r: %r (%r)" % (t, val, pos, dir))
    return pos

test_input = '''F10
N3
F7
R90
F11'''
print(run_p2(get_input(test_input)))
print(run_p2(get_input(get_raw_input())))