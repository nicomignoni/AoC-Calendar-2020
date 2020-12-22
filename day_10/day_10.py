with open('day_10.txt') as f:
    adapters = [int(adapter) for adapter in f.readlines()]

plug = 0
device_adapter = max(adapters) + 3
jolts = sorted([plug] + adapters + [device_adapter])

'''
ones   = 0
threes = 0
for i in range(1, len(jolts)):
    if jolts[i] - jolts[i - 1] == 3:
        threes += 1
    elif jolts[i] - jolts[i - 1] == 1:
        ones += 1

print(ones * threes)
'''

c = '0 '
ptr = 1
while ptr <= len(jolts) - 1:
    if jolts[ptr] - jolts[ptr - 1] == 3:
        c = c[:-1]
        c += ' ' + str(jolts[ptr - 1]) + ' ' + str(jolts[ptr]) + ' '
        ptr += 1
    elif jolts[ptr] - jolts[ptr - 1] < 3:
        c += '_'
        ptr += 1

print(2 ** (c.count('_') + c.count('__')) * (7 * c.count('___')))
        
'''
# Minimum adapter chain

ptr = 1
old_ptr = 0
chain = [jolts[0]]
while ptr < len(jolts) - 1:
    if jolts[ptr] - jolts[old_ptr] == 3:
        chain.append(jolts[ptr])
        old_ptr = ptr
    elif jolts[ptr] - jolts[old_ptr] > 3:
        ptr -= 1
        chain.append(jolts[ptr])
        old_ptr = ptr
    ptr += 1
'''
