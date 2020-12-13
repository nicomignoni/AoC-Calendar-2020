tree = '#'

right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

with open('day_3.txt') as f:
    m = f.read().splitlines()

results = list()

for i in range(len(right)):
    row_len, col_len = len(m), len(m[0])
    prev_row, prev_col = 0, 0
    tree_count = 0

    for l in range(row_len // down[i] - 1):
        
        next_row = prev_row + down[i]
        next_col = (prev_col + right[i]) % col_len
        
        if m[next_row][next_col] == tree:
            tree_count += 1

        prev_row, prev_col = next_row, next_col

    results.append(tree_count)
        
prod = 1
for result in results: prod *= result
