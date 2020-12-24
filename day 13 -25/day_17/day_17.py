import numpy as np

with open('day_17.txt') as f:
    plane = np.array([[1 if c == '#' else 0 for c in row] for row in f.read().splitlines()])

def neighbors(i, j, w):
    global X, Y, Z
    return [(i + a, j + b, w + c) for a in range(-1,2) for b in range(-1,2) for c in range(-1,2) \
            if not (a == 0 and b == 0 and c == 0) and \
            i + a >= 0 and i + a < X and j + b >= 0 and j + b < Y and w + c >= 0 and w + c < Z]

def active_neighbors(i, j, w):
    global box
    return sum([1 for neighbor in neighbors(i, j, w) if box[neighbor] == 1])
        

ITER   = 6
INIT_Y = len(plane)
INIT_X = len(plane[0])
INIT_Z = 1

X = 2*ITER + INIT_X
Y = 2*ITER + INIT_Y
Z = 2*ITER + INIT_Z 

# Create the box
box = np.zeros((X, Y, Z), np.int8)
box[ITER: ITER + INIT_X, ITER: ITER + INIT_Y, ITER] = plane

# Simulate
for iteration in range(ITER):
    next_box = np.copy(box)
    for i in range(X):
        for j in range(Y):
            for w in range(Z):
                active = active_neighbors(i, j, w)
                if box[i, j, w] == 1 and (active < 2 or active > 3):
                    next_box[i, j, w] = 0
                elif box[i, j, w] == 0 and active == 3:
                    next_box[i, j, w] = 1
    box = next_box

unique, counts = np.unique(box, return_counts=True)
print(dict(zip(unique, counts)))
