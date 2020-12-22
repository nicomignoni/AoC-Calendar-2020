with open('day_7.txt') as f:
    rules = f.readlines()

# Parse the rules {color : {*color: num_items}}
parsed_rules = dict()
for rule in rules:
    rule_color, admissibilities = rule.split(' bags contain ')
    parsed_rules[rule_color] = {}

    for adm in admissibilities.split(', '):
        admitted_color = ' '.join(adm.split()[1:3])
        if adm.split()[0] != 'no':
            admitted_num = int(adm.split()[0])
            parsed_rules[rule_color][admitted_color] = admitted_num
        
implications = {'shiny gold'}
current_lenght = len(implications)
while True:
    unfinished = False
    for rule_color, rule in parsed_rules.items():
        for admitted_color in rule.keys():
            if admitted_color in implications:
                implications.add(rule_color)
    if len(implications) > current_lenght:
        current_lenght = len(implications)
    else:
        break

print('Bags that can eventually contain a shiny bag: {}'.format(
    len(implications) - 1))


# Breadth-first spanning tree geenration
depth = 0
tree = {'shiny gold' : {'edges': parsed_rules['shiny gold'],
                        'depth': depth,
                        'total': 0}}
colors_to_check = [color for color in tree['shiny gold']['edges']]

while colors_to_check:
    next_colors = list()
    depth += 1
    for color in colors_to_check:
        tree[color] = {}
        tree[color]['edges'] = parsed_rules[color]
        tree[color]['depth'] = depth
        tree[color]['total'] = 1
        next_colors.extend([color for color in tree[color]['edges']])
    colors_to_check = next_colors

# Going up
while depth >= 0:
    depth -= 1
    colors_to_check = [color for color in tree if tree[color]['depth'] == depth]
    for color in colors_to_check:
        tree[color]['total'] += sum([tree[color]['edges'][color_child] * tree[color_child]['total']
                                    for color_child in tree[color]['edges'].keys()])

print('Individual bags required inside your single shiny gold bag: {}'.format(
    tree['shiny gold']['total']))
        
            
        
    
    
