import re

with open('day_4.txt') as f:
    docs = f.read().split('\n\n')

mandatories = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0

def birth_rule(doc):
    birth_year = re.findall(r'byr:\S*', doc)[0].split(':')[1]
    if len(birth_year) == 4 and (int(birth_year) >= 1920 and int(birth_year) <= 2002):
        return True
    else:
        return False

def issue_rule(doc):
    issue_year = re.findall(r'iyr:\S*', doc)[0].split(':')[1]
    if len(issue_year) == 4 and (int(issue_year) >= 2010 and int(issue_year) <= 2020):
        return True
    else:
        return False

def expiration_rule(doc):
    exp_year = re.findall(r'eyr:\S*', doc)[0].split(':')[1]
    if len(exp_year) == 4 and (int(exp_year) >= 2020 and int(exp_year) <= 2030):
        return True
    else:
        return False

def height_rule(doc):
    height = re.findall(r'hgt:\S*', doc)[0].split(':')[1]
    if len(height) <= 2: return False
    metric = height[-2:]
    value  = int(height[:-2])
    if (height[-2:] == 'cm' and value >= 150 and value <= 193) or \
       (height[-2:] == 'in' and value >= 59 and value <= 76):
        return True
    else:
        return False

def hair_rule(doc):
    color = re.findall(r'hcl:\S*', doc)[0].split(':')[1]
    letters = 'abcdef'
    numbers = '0123456789'
    if color[0] == '#' and all([(s in letters + numbers) for s in color[1:]]):
        return True
    else:
        return False

def eye_rule(doc):
    eye = re.findall(r'ecl:\S*', doc)[0].split(':')[1]
    colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if len(eye) == 3 and eye in colors: return True
    else: return False

def passport_rule(doc):
    passport = re.findall(r'pid:\S*', doc)[0].split(':')[1]
    numbers = '0123456789'
    if len(passport) == 9 and all([n in numbers for n in passport]):
        return True
    else:
        return False


for doc in docs:
    if all([field in doc for field in mandatories]) and \
       birth_rule(doc)      and \
       issue_rule(doc)      and \
       expiration_rule(doc) and \
       height_rule(doc)     and \
       hair_rule(doc)       and \
       eye_rule(doc)        and \
       passport_rule(doc):
        count += 1

print(count)
    
    
