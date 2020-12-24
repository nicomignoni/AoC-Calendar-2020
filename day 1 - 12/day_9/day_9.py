with open('day_9.txt') as f:
    nums = [int(n) for n in f.readlines()]

prmb = nums[:25] 
sums = [prmb[i] + prmb[j] for i in range(25) for j in range(i + 1, len(prmb))]

next_index = len(prmb) - 1
def update_prmb():
    global prmb, next_index
    while True:
        next_index += 1
        prmb.pop(0)
        prmb.append(nums[next_index])
        yield 

def update_sums():
    global sums, prmb
    while True:
        sums = sums[len(prmb) - 1:]
        sums_with_new_n = [prmb[-1] + n for n in prmb[:-1]]

        insert_index = 0
        for i, n in enumerate(sums_with_new_n):
            insert_index += len(prmb) - (i + 1) 
            sums.insert(insert_index - 1, n)
        yield
          

for i, n in enumerate(nums[len(prmb):]):
    if n not in sums:
        print(n)
        break
    else:
        print('ID: {}, n: {}, finded in "sums".'.format(i + len(prmb), n))
        next(update_prmb())
        next(update_sums())
    
# part 1 ans = 400480901
ans = 400480901

buffer = [nums[0]]
for n in nums[1:]:
    buffer.append(n)
    print('Buffer: {}, sum: {}'.format(buffer, sum(buffer)))
    while sum(buffer) > ans:
        buffer.pop(0)
    if sum(buffer) == ans:
        break
