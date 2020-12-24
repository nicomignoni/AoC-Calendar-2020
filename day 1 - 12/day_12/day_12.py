from math import fabs

with open('day_12.txt') as f:
    prog = f.read().splitlines()

current_direction = 0

ship = {0: 0, # E
        1: 0, # N 
        2: 0, # W
        3: 0} # S

dir2num = {'E': 0,
           'N': 1,
           'W': 2,
           'S': 3}

# Part 1
for line in prog:
    cmd, value = line[0], int(line[1:])
    if cmd == 'F':
        ship[current_direction] += value
        # print('Move {} {}'.format(value, current_direction))
    elif cmd in dir2num:
        ship[dir2num[cmd]] += value
        # print('Move {} {}'.format(value, dir2num[cmd]))
    elif cmd == 'L':
        current_direction = (current_direction + value // 90) % 4
        # print('Change direction to {}'.format(current_direction))
    elif cmd == 'R': 
        current_direction = (current_direction + 4 - value // 90) % 4
        # print('Change direction to {}'.format(current_direction))

print(fabs(ship[0] - ship[2]) + fabs(ship[1] - ship[3]))

#Part 2
current_direction = 0

ship = {0: 0, # E
        1: 0, # N 
        2: 0, # W
        3: 0} # S

# Relative to the ship
way = {0: 10, # E
       1: 1,  # N 
       2: 0,  # W
       3: 0}  # S

for line in prog:
    cmd, value = line[0], int(line[1:])
    if cmd == 'F':
        for direction in range(4):
            ship[direction] += value * way[direction]
    elif cmd in dir2num:
        way[dir2num[cmd]] += value
    elif cmd == 'R':
        for time in range(value // 90):
            way[0], way[1], way[2], way[3] = way[1], way[2], way[3], way[0]
    elif cmd == 'L':
        for time in range(value // 90):
            way[0], way[1], way[2], way[3] = way[3], way[0], way[1], way[2]

print(fabs(ship[0] - ship[2]) + fabs(ship[1] - ship[3]))
        
