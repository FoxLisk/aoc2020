def parse_input(lines):
    answers = []
    current = 0b11111111111111111111111111
    for l in lines:
        l = l.strip()
        if not l:
            answers.append(current)
            current = 0b11111111111111111111111111
        else:
            t = 0
            for c in l:
                t |= 1 << ord(c) - ord('a')
            current &= t
    if current:
        answers.append(current)
    return answers

print(parse_input('''abc

a
b
c

ab
ac

a
a
a
a

b'''.splitlines()))

with open('day6_input.txt') as f:
    answers = (parse_input(f.readlines()))

print(sum(bin(a).count('1') for a in answers))
