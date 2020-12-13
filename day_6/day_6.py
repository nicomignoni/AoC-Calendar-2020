with open('day_6.txt') as f:
    groups = f.read().split('\n\n')

total_part_1 = 0
total_part_2 = 0
for group in groups:
    total_part_1 += len(set(group.replace('\n', '')))
    total_part_2 += len(set.intersection(*[set(person)
                                           for person in group.split('\n')]))
    
