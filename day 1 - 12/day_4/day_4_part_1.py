import re

with open('day_4.txt') as f:
    docs = f.read().split('\n\n')

mandatories = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0

for doc in docs:
    if all([attribute in doc for attribute in mandatories]):
        count += 1

print(count)
    
    
