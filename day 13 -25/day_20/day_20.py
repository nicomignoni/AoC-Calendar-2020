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

IDS = list(tiles.keys())
for i in range(len(IDS)):
    for j in range(i, len(IDS)):
        if right_border(tiles[IDS[i]]['tile']) == left_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['right_conf'] = IDS[j]
            tiles[IDS[j]]['left_conf'] = IDS[i]
        elif right_border(tiles[IDS[j]]['tile']) == left_border(tiles[IDS[i]]['tile']):
            tiles[IDS[i]]['right_conf'] = IDS[i]
            tiles[IDS[j]]['left_conf'] = IDS[j]
        elif upper_border(tiles[IDS[i]]['tile']) == lower_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['upper_conf'] = IDS[j]
            tiles[IDS[j]]['lower_conf'] = IDS[i]
        elif upper_border(tiles[IDS[j]]['tile']) == lower_border(tiles[IDS[i]]['tile']):
            tiles[IDS[j]]['upper_conf'] = IDS[i]
            tiles[IDS[i]]['lower_conf'] = IDS[j]

        elif right_border(flipud(tiles[IDS[i]]['tile'])) == left_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['right_conf'] = IDS[j]
            tiles[IDS[j]]['left_conf'] = IDS[i]
        elif right_border(tiles[IDS[j]]['tile']) == left_border(flipud(tiles[IDS[i]]['tile'])):
            tiles[IDS[i]]['right_conf'] = IDS[i]
            tiles[IDS[j]]['left_conf'] = IDS[j]
        elif upper_border(flipud(tiles[IDS[i]]['tile'])) == lower_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['upper_conf'] = IDS[j]
            tiles[IDS[j]]['lower_conf'] = IDS[i]
        elif upper_border(tiles[IDS[j]]['tile']) == lower_border(flipud(tiles[IDS[i]]['tile'])):
            tiles[IDS[j]]['upper_conf'] = IDS[i]
            tiles[IDS[i]]['lower_conf'] = IDS[j]

        elif right_border(fliplr(tiles[IDS[i]]['tile'])) == left_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['right_conf'] = IDS[j]
            tiles[IDS[j]]['left_conf'] = IDS[i]
        elif right_border(tiles[IDS[j]]['tile']) == left_border(fliplr(tiles[IDS[i]]['tile'])):
            tiles[IDS[i]]['right_conf'] = IDS[i]
            tiles[IDS[j]]['left_conf'] = IDS[j]
        elif upper_border(fliplr(tiles[IDS[i]]['tile'])) == lower_border(tiles[IDS[j]]['tile']):
            tiles[IDS[i]]['upper_conf'] = IDS[j]
            tiles[IDS[j]]['lower_conf'] = IDS[i]
        elif upper_border(tiles[IDS[j]]['tile']) == lower_border(fliplr(tiles[IDS[i]]['tile'])):
            tiles[IDS[j]]['upper_conf'] = IDS[i]
            tiles[IDS[i]]['lower_conf'] = IDS[j]

        elif right_border(flipud(tiles[IDS[i]]['tile'])) == left_border(fliplr(tiles[IDS[j]]['tile'])):
            tiles[IDS[i]]['right_conf'] = IDS[j]
            tiles[IDS[j]]['left_conf'] = IDS[i]
        elif right_border(fliplr(tiles[IDS[j]]['tile'])) == left_border(flipud(tiles[IDS[i]]['tile'])):
            tiles[IDS[i]]['right_conf'] = IDS[i]
            tiles[IDS[j]]['left_conf'] = IDS[j]
        elif upper_border(flipud(tiles[IDS[i]]['tile'])) == lower_border(fliplr(tiles[IDS[j]]['tile'])):
            tiles[IDS[i]]['upper_conf'] = IDS[j]
            tiles[IDS[j]]['lower_conf'] = IDS[i]
        elif upper_border(fliplr(tiles[IDS[j]]['tile'])) == lower_border(flipud(tiles[IDS[i]]['tile'])):
            tiles[IDS[j]]['upper_conf'] = IDS[i]
            tiles[IDS[i]]['lower_conf'] = IDS[j]

corners = [tile_id for tile_id in tiles if [val for val in tiles[tile_id].values()].count(None) == 2]
            
        
     
        


