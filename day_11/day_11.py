from copy import deepcopy

with open('day_11.txt') as f:
    layout = [[sym for sym in row] for row in f.read().splitlines()]

num_rows, num_cols = len(layout), len(layout[0])

empty_seat    = 'L'
occupied_seat = '#'
floor         = '.'

def adjacent_indices(i, j):
    global num_rows, num_cols
    indices = [(i + h, j + k) for k in range(-1,2) for h in range(-1,2) if not (h == 0 and k == 0)
               and i + h >= 0 and j + k >= 0 and i + h <= num_rows - 1 and j + k <=  num_cols - 1]
    return indices

def visible_indices(layout, i, j):
    global num_rows, max_cols
    indices = list()
    for index in adjacent_indices(i,j):
        found = True
        if layout[index[0]][index[1]] in {empty_seat, occupied_seat}: indices.append(index)
        else:
            increment_i = index[0] - i
            increment_j = index[1] - j
            while not layout[index[0]][index[1]] in {empty_seat, occupied_seat}:
                index = (index[0] + increment_i, index[1] + increment_j)
                if index[0] < 0 or index[0] > num_rows - 1 or \
                   index[1] < 0 or index[1] > num_cols - 1:
                    found = False
                    break
            if found: indices.append(index)
    return indices
        

def num_occupied_adj_seats(layout, i, j):
    return sum([1 for row, col in adjacent_indices(i,j) if layout[row][col] == occupied_seat])

def num_occupied_vis_seats(layout, i, j):
    return sum([1 for row, col in visible_indices(layout, i, j) if layout[row][col] == occupied_seat])

next_layout = [['.' for i in range(num_cols)] for j in range(num_rows)]

# Part 1
while True:
    something_changed = False
    for i in range(num_rows):
        for j in range(num_cols):
            if layout[i][j] == floor:
                continue
            elif layout[i][j] == empty_seat and num_occupied_adj_seats(layout, i, j) == 0:
                next_layout[i][j] = occupied_seat          
                something_changed = True
            elif layout[i][j] == occupied_seat and num_occupied_adj_seats(layout, i, j) >= 4:
                next_layout[i][j] = empty_seat
                something_changed = True
    
    if not something_changed:
        break
    else:
        layout = deepcopy(next_layout)
        iterations += 1

print(sum([row.count(occupied_seat) for row in layout]))


# Part 2
while True:
    something_changed = False
    for i in range(num_rows):
        for j in range(num_cols):
            if layout[i][j] == floor:
                continue
            elif layout[i][j] == empty_seat and num_occupied_vis_seats(layout, i, j) == 0:
                next_layout[i][j] = occupied_seat          
                something_changed = True
            elif layout[i][j] == occupied_seat and num_occupied_vis_seats(layout, i, j) >= 5:
                next_layout[i][j] = empty_seat
                something_changed = True
    
    if not something_changed:
        break
    else:
        layout = deepcopy(next_layout)

print(sum([row.count(occupied_seat) for row in layout]))
    
    
