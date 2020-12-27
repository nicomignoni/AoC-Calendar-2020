with open("day_21_test.txt") as f:
    recepies = f.read().splitlines()

ing2id = dict()
all2id = dict()

allergens_per_recepie = list()

def print_mat(mat):
    for row in mat:
        print(row)

# Build the ing -> id, all -> id dictionaries
for recepie in recepies:
    ingredients, allergens = recepie.split(" (contains ")
    for ingredient in ingredients.split():
        if ingredient not in ing2id:
            ing2id[ingredient] = len(ing2id)

    allergens_in_recepie = set()
    for allergen in allergens.split():
        if allergen[:-1] not in all2id:
            all2id[allergen[:-1]] = len(all2id)
        allergens_in_recepie.add(all2id[allergen[:-1]])
    allergens_per_recepie.append(allergens_in_recepie)

# Build the matrix (each row recepie, each column ingredient, each cell the possible allergen)
mat = list()
for i in range(len(recepies)):
    mat.append([set() for j in range(len(ing2id))])

for i, recepie in enumerate(recepies):
    ingredients, allergens = recepie.split(" (contains ")
    for ingredient in ingredients.split():
        for allergen in allergens.split(): mat[i][ing2id[ingredient]].add(all2id[allergen[:-1]])


# Checking ingredients
free = set()
for j in range(len(mat[0])):
    contradictions = set()
    possible_ingredient_allergens = set.union(*[mat[i][j] for i in range(len(mat))])
    for i in range(len(mat)):
        # print("Cell: {}, Poss ing all: {}, Rec all: {}".format(mat[i][j], possible_ingredient_allergens, allergens_per_recepie[i]))
        if mat[i][j].intersection(possible_ingredient_allergens) != allergens_per_recepie[i].intersection(possible_ingredient_allergens):
            for allergen in allergens_per_recepie[i].intersection(possible_ingredient_allergens): contradictions.add(allergen)
    if contradictions == possible_ingredient_allergens:
        free.add(j)
        for i in range(len(mat)): mat[i][j] = set() 

# Counting the occurrences
count = 0
for j in free:
    count += sum([1 for i in range(len(mat)) if mat[i][j]])
    
         

