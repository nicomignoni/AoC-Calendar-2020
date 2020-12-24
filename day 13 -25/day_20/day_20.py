from math import sqrt

with open('day_20.txt') as f:
    inpt = f.read().splitlines()

def right_border(tile):
    return [row[-1] for row in tile]

def left_border(tile):
    return [row[0] for row in tile]

def upper_border(tile):
    return tile[0]

def lower_border(tile):
    return tile[-1]

def fliplr(tile):
    return [row[::-1] for row in tile]

def flipud(tile):
    return [tile[i] for i in range(ROWS - 1, -1, -1)]

def print_tile(tile):
    for row in tile:
        print(row)

LINES = len(inpt)
ROWS  = 10

# Create the tiles dictionary
tiles   = dict()
indices = list()
for i in range(0, LINES, ROWS + 2):
    _, tile_id = inpt[i][:-1].split()
    indices.append(int(tile_id))
    tiles[int(tile_id)] = {'tile': inpt[i + 1: i + ROWS + 1],
                           'upper_conf': None,
                           'lower_conf': None,
                           'right_conf': None,
                           'left_conf' : None,
                           }

SIDE = sqrt(len(tiles))

for i in range(LINES):
    for j in range(i, LINES):
        if right_border(tiles[i]['tiles']) == left_border(tiles[j]['tiles']):
            tiles[i]['right_conf'] = j
            tiles[j]['left_conf'] = i
        elif 
     
        


