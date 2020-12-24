with open("day_24.txt") as f:
    strings = f.read().splitlines()

coords = {'e' : (1, 0),
          'w' : (-1, 0),
          'ne': (0.5, 0.5),
          'nw': (-0.5, 0.5),
          'se': (0.5, -0.5),
          'sw': (-0.5, -0.5)
          }

# Colors: 1 white, 0 black
tiles = dict()

for string in strings:
    coord = [0, 0]
    i = 0
    while i < len(string):
        if string[i:i+2] == 'ne':
            coord[0] += coords['ne'][0]
            coord[1] += coords['ne'][1]
            i += 2
        elif string[i:i+2] == 'nw':
            coord[0] += coords['nw'][0]
            coord[1] += coords['nw'][1]
            i += 2
        elif string[i:i+2] == 'se':
            coord[0] += coords['se'][0]
            coord[1] += coords['se'][1]
            i += 2
        elif string[i:i+2] == 'sw':
            coord[0] += coords['sw'][0]
            coord[1] += coords['sw'][1]
            i += 2
        elif string[i] == 'e':
            coord[0] += coords['e'][0]
            coord[1] += coords['e'][1]
            i += 1
        elif string[i] == 'w':
            coord[0] += coords['w'][0]
            coord[1] += coords['w'][1]
            i += 1
    coord = tuple(coord)
    if coord in tiles:
        tiles[coord]['color'] = (tiles[coord]['color'] + 1) % 2
    else:
        tiles[coord] = {'color': 0}

black_tiles = sum([1 for value in tiles.values() if value['color'] == 0])
print('Black tiles: {}'.format(black_tiles))

# Part 2 (to be reformatted)
tiles_to_add = list()
for coord in tiles:
    for direction in coords.values():
        neighbor = (coord[0] + direction[0], coord[1] + direction[1])
        if neighbor not in tiles: tiles_to_add.append(neighbor)
for coord in tiles_to_add:
    tiles[coord] = {'color': 1}
        
def black_tiles_around(coord):
    count = 0
    for direction in coords.values():
        neighbor = (coord[0] + direction[0], coord[1] + direction[1])
        if neighbor in tiles and tiles[neighbor]['color'] == 0:
            count += 1
        elif neighbor not in tiles:
            tiles_to_add.append(neighbor)
    return count

for i in range(100):
    tiles_to_add    = list()
    tiles_to_switch = list()
    for coord in tiles:
        black_tile_neigh = black_tiles_around(coord)
        if (tiles[coord]['color'] == 0 and (black_tile_neigh == 0 or black_tile_neigh > 2)) or \
           (tiles[coord]['color'] == 1 and black_tile_neigh == 2):
            tiles_to_switch.append(coord)

    for coord in tiles_to_switch:
        tiles[coord]['color'] = (tiles[coord]['color'] + 1) % 2

    for coord in tiles_to_add:
        tiles[coord] = {'color': 1}

black_tiles = sum([1 for value in tiles.values() if value['color'] == 0])
print('Black tiles (after 100 days): {}'.format(black_tiles))
    
    
