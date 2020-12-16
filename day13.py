import math


def parse_input(r):
    t0 = int(r[0])
    ids = [
        (i, int(x)) for i, x in enumerate(r[1].split(','))
        if x != 'x'
    ]
    return t0, ids

def run_p1(t0, ids):
    wait = 999999999
    best = None
    for _, id in ids:
        # t0 % id is the number of steps into the id's departure we are.
        # i.e. on t0 = 6, id = 5, 6 % 5 means the bus is 1 step into its
        # next cycle.
        _wait = id - (t0 % id)
        if _wait < wait:
            wait = _wait
            best = id
    return wait, best

def run_p2(ids):
    '''
    we need t such that
    t - (t % ids[i]) == i
    for all i

        (zero-indexed)
    so

    t = k_i*ids[i] + i
    (t - i) = k_i*ids[i]

    for example:
    7,13,x,x,59,x,31,19

    (t - 0) = 0 (mod 7)
    (t - 1) = 0 (mod 13)
    (t - 4) = 0 (mod 59)
    (t - 6) = 0 (mod 31)
    (t - 7) = 0 (mod 19)

    ... or

    t = k_0 * 7
    t = k_1 * 13 + 1

    k_0 * 7 = k_1 * 13 + 1

    solns are like: 14, 105, 196
    7*2, 5*3*7, 2*2*7*7

    ok one thing we've learned is the distance b/w 2 consecutive numbers that work
    is the same.
    what is 91? it's 7 * 13. tHAT SEEMS PRETTY OBVIOUS

    in fact once you have n such that n = k_1 (mod m_1) and n = k_2 (mod m_2), the only way to not change that is by
    adding a multiple of lcm(m1, m2)

    so we can build up an answer by finding the minimum answer for the first guy, then adding more as we go on, i guess?

    ok this is wrong b/c we want 77, 168, etc; i.e. when n % 7 == 0 still but n % 13 == 12 (i.e. 13 - 1)
    but the rest of the analysis is fine
    '''

    def lcm(a, b):
        return a*b // math.gcd(a, b)

    ans, min_div = ids[0]
    divs = [min_div]
    cur_lcm = min_div
    for i, id in ids[1:]:
        while ans % id != ((-i) % id):
            ans += cur_lcm
        new_lcm = lcm(cur_lcm, id)
        if new_lcm != cur_lcm * id:
            print('woah')
            # this implies not everyone is coprime which seems... unlikely given how friendly inputs have been so far
        cur_lcm = new_lcm
        print(ans)
    return ans

ti, idsi = parse_input('''939
7,13,x,x,59,x,31,19'''.splitlines())
ti, idsi = parse_input(open('day13_input.txt').readlines())
#print(run_p1(ti, idsi))
#wait, best = run_p1(ti, idsi)
#print(wait*best)

print(run_p2(idsi))