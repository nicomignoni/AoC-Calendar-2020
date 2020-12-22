import numpy as np

with open('day_17.txt') as f:
    plane = np.array([[1 if c == '#' else 0 for c in row] for row in f.read().splitlines()])

def neighbors(i, j, w, h):
    global X, Y, Z, K
    return [(i + a, j + b, w + c, h + d) for a in range(-1,2) for b in range(-1,2) for c in range(-1,2) for d in range(-1, 2)\
            if not (a == 0 and b == 0 and c == 0 and d == 0) and \
            i + a >= 0 and i + a < X and j + b >= 0 and j + b < Y and w + c >= 0 and w + c < Z and h + d >= 0 and h + d < K]

def active_neighbors(i, j, w, h):
    global box
    return sum([1 for neighbor in neighbors(i, j, w, h) if box[neighbor] == 1])
        

ITER   = 6
INIT_Y = len(plane)
INIT_X = len(plane[0])
INIT_Z = 1
INIT_K = 1

X = 2*ITER + INIT_X
Y = 2*ITER + INIT_Y
Z = 2*ITER + INIT_Z
K = 2*ITER + INIT_K

# Create the box
box = np.zeros((X, Y, Z, K), np.int8)
box[ITER: ITER + INIT_X, ITER: ITER + INIT_Y, ITER, ITER] = plane

# Simulate
for iteration in range(ITER):
    next_box = np.copy(box)
    for i in range(X):
        for j in range(Y):
            for w in range(Z):
                for h in range(K):
                    active = active_neighbors(i, j, w, h)
                    if box[i, j, w, h] == 1 and (active < 2 or active > 3):
                        next_box[i, j, w, h] = 0
                    elif box[i, j, w, h] == 0 and active == 3:
                        next_box[i, j, w, h] = 1
    box = next_box

unique, counts = np.unique(box, return_counts=True)
print(dict(zip(unique, counts)))
