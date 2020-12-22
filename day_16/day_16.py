with open('day_16.txt') as f:
    notes = f.read().splitlines()

# Parsing the input
ticket_line_idx = None
rules = dict()
nearby_tickets = list()
for i, line in enumerate(notes):
    if line == 'your ticket:':
        ticket_line_idx = i + 1
        my_ticket = [int(n) for n in notes[ticket_line_idx].split(',')]
    elif line == 'nearby tickets:':
        for j in range(i + 1, len(notes)):
            nearby_tickets.append([int(n) for n in notes[j].split(',')])
        break
    elif line == '' or i == ticket_line_idx:
        continue
    else:
        rule, val = line.split(': ')
        rules[rule] = [[int(n) for n in inter.split('-')]
                       for inter in val.split(' or ')]

 
# Part 1

# Make a global range
global_range      = list()
tickets_to_delete = list()
for element in rules.values():
    for exts in element:
        global_range.extend(list(range(exts[0], exts[1] + 1)))
global_range = set(global_range)

wrong_fields = list()
for i, ticket in enumerate(nearby_tickets):
    for n in ticket:
        if n not in global_range:
            wrong_fields.append(n)
            tickets_to_delete.append(i)


# Part 2

candidates = list()
for i in sorted(tickets_to_delete, reverse=True):
    del nearby_tickets[i]

for ticket in [my_ticket] + nearby_tickets:
    row = list()
    for n in ticket:
        row.append({rule for rule, val in rules.items() if n in range(val[0][0], val[0][1] + 1) or \
                                                           n in range(val[1][0], val[1][1] + 1)})
    candidates.append(row)        

admissibles = candidates[0]
for ticket in candidates:
    for i in range(len(ticket)):
        admissibles[i] = admissibles[i].intersection(ticket[i])

i = 0
while not all([len(element) == 1 for element in admissibles]):
    if len(admissibles[i]) == 1:
        for j in range(len(admissibles)):
            if j != i: admissibles[j] -= admissibles[i]
    i = (i + 1) % len(admissibles)
