with open('day_13.txt') as f:
    times = f.read().splitlines()

timestamp, buses = int(times[0]), times[1].split(',')
closest_timestamp = dict()

'''
# Part 1
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        closest_timestamp[bus] = timestamp - (timestamp % bus) + bus
'''

'''
The problem of part 2 consist in finding the smallest T such that

T      = 0 mod 41
T + 34 = 0 mod 37
T + 39 = 0 mod 541
T + 46 = 0 mod 23
T + 50 = 0 mod 13
T + 53 = 0 mod 17
T + 64 = 0 mod 29
T + 65 = 0 mod 983
T + 83 = 0 mod 19

is satisfied. The system can also be written as

T      = 41 * a
T + 34 = 37 * b
T + 39 = 541 * c
T + 46 = 23 * d 
T + 50 = 13 * e
T + 53 = 17 * f
T + 64 = 29 * g
T + 65 = 983 * h
T + 83 = 19 * i

'''

# Part 2
line = times[1].split(',')
jump = 0
jumps  = [0]
moduli = [int(line[0])]
for i in range(1, len(line)):
    if line[i] == 'x':
        jump += 1
    else:
        jumps.append(jumps[-1] + jump)
        jump = 0
        moduli.append(int(line[i]))

v = 0
c = sum(jumps)
while True:
    comb = format(v, '09d')
    t = sum([moduli[i] * int(comb[i]) for i in range(len(comb))]) - c
    if t > 0 and t % 9 == 0:
        break
        print(t)
    else: v += 1


