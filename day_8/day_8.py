from copy import deepcopy

with open('day_8.txt') as f:
    ins = f.read().splitlines()

ptr = 0
acc = 0
flags = [0] * len(ins)

def execute(line):
    global ptr, acc
    instr, val = line.split()
    if instr == 'nop':
        # print('Instr. NOP, PTR @ {}: No instruction executed'.format(ptr))
        ptr += 1
    elif instr == 'acc':
        # print('Instr. ACC, PTR @ {}: Delta {}, ({})'.format(ptr, int(val), acc + int(val)))
        acc += int(val)
        ptr += 1
    elif instr == 'jmp':
        # print('Instr. JMP, PTR @ {}: Jumping at line {}'.format(ptr, ptr + int(val)))
        ptr += int(val)

# First execution (Part 1)
'''
while True:
    if flags[ptr] == 1:
        print(acc)
        break
    else:
        flags[ptr] = 1
        execute(ins[ptr])
'''

# Second execution (Part 2)

def ins_gen(ins):
    for i in range(len(ins)):
        if ins[i][:3] == 'nop':
            new_ins = deepcopy(ins)
            new_ins[i] = new_ins[i].replace('nop', 'jmp')
            yield new_ins
        elif ins[i][:3] == 'jmp':
            new_ins = deepcopy(ins)
            new_ins[i] = new_ins[i].replace('jmp', 'nop')
            yield new_ins

for mod_ins in ins_gen(ins):
    
    ptr = 0
    acc = 0
    flags = [0] * len(ins) 

    while True:
        if ptr == len(ins):
            print(acc)
            break
        elif flags[ptr] == 1:
            break
        else:
            flags[ptr] = 1
            execute(mod_ins[ptr])
