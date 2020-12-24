import numpy as np

with open('day_1.txt') as f:
    nums = np.array([int(n) for n in f.readlines()])

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 2020:
            result = nums[i] * nums[j]
            print('E1: {}, E2: {}'.format(nums[i], nums[j]))
            break

print(result)
