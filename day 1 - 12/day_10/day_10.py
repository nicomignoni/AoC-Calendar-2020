import re

with open('day_10.txt') as f:
    adapters = [int(adapter) for adapter in f.readlines()]

plug = 0
device_adapter = max(adapters) + 3
jolts = sorted([plug] + adapters + [device_adapter])

# Part 1
ones   = 0
threes = 0
for i in range(1, len(jolts)):
    if jolts[i] - jolts[i - 1] == 3:
        threes += 1
    elif jolts[i] - jolts[i - 1] == 1:
        ones += 1

print(ones * threes)

# Part 2
c = ['0']
ptr = 1
while ptr <= len(jolts) - 1:
    if jolts[ptr] - jolts[ptr - 1] == 3:
        c = c[:-1]
        if c[-1] == jolts[ptr - 1]: c.append(str(jolts[ptr]))
        else: c.extend([str(jolts[ptr - 1]), str(jolts[ptr])])
        ptr += 1
    elif jolts[ptr] - jolts[ptr - 1] < 3:
        c.append('_')
        ptr += 1

c_as_string = ''.join(c)
ones   = len(re.findall(r'[0-9]_[0-9]', c_as_string))
twos   = len(re.findall(r'[0-9]__[0-9]', c_as_string))
threes = len(re.findall(r'[0-9]___[0-9]', c_as_string))

# There has to be a better way to put it
print(2 ** (ones) * (2 ** 2) ** (twos) * (2 ** 3 - 1) ** (threes))


