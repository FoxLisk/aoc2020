def parse_input(lines):
    instrs = []
    for l in lines:
        l = l.strip()
        instr, arg = l.split(' ')
        instrs.append((instr, int(arg)))
    return instrs

with open('day8_input.txt') as f:
    instrs = parse_input(f.readlines())

_instrs = parse_input(
'''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines())

def run_instrs(instrs):
    visited = set()
    acc = 0
    inst_ptr = 0
    while True:
        if inst_ptr in visited:
            return ('loop',  acc)
            break
        if inst_ptr >= len(instrs):
            return 'EOF', acc
        visited.add(inst_ptr)
        inst, arg = instrs[inst_ptr]
        if inst == 'nop':
            inst_ptr += 1
        elif inst == 'acc':
            acc += arg
            inst_ptr += 1
        elif inst == 'jmp':
            inst_ptr += arg
        else:
            raise ValueError('bad inst %r' % inst)

for i in range(len(instrs)):
    op, arg = instrs[i]
    if op == 'nop':
        t, acc = run_instrs(instrs[:i] + [('jmp', arg)] + instrs[i+1:])
        if t == 'EOF':
            print(acc)
            break
    elif op == 'jmp':
        t, acc = run_instrs(instrs[:i] + [('nop', arg)] + instrs[i+1:])
        if t == 'EOF':
            print(acc)
            break
