from copy import deepcopy

with open('day_19.txt') as f:
    lines = f.read().splitlines()

rules      = dict()
messages   = list()
base_rules = set()

i = 0
while lines[i] != '':
    index, rule = lines[i].split(': ')
    if rule[1].isalpha():
        rules[index] = rule[1]
        base_rules.add(index)
    else:
        rules[index] = [subrule.split() for subrule in rule.split(' | ')]
    i += 1

i += 1
while i < len(lines):
    messages.append(lines[i])
    i += 1

base = rules['0']
i = 0
while i < len(base):
    j = 0
    while j < len(base[i]):
        if base[i][j] in base_rules:
            base[i][j] = rules[base[i][j]]
            j += 1
        elif not base[i][j].isalpha():
            ref_explicit = deepcopy(rules[base[i][j]])
            for w in range(len(ref_explicit)):
                ref_explicit[w] = base[i][:j] + ref_explicit[w] + base[i][j + 1:]
            del base[i]
            for subrule in ref_explicit[::-1]: base.insert(i, subrule)
        else:
            j += 1
    i += 1

print('Start checking')

counter = 0
base = {''.join(subbase) for subbase in base}
for message in messages:
    not_in = False
    for rule in base:
        if rule not in message:
            not_in = True
            break
    if not not_in: counter += 1
            
