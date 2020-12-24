import time

s = time.time()

inpt = '389125467'
cups = [int(cup) for cup in inpt] + [i for i in range(10, 10 ** 6 + 1)]

MAX = max(cups)
MIN = min(cups)

# Part 1
current_cup_id = 0
current_cup = cups[current_cup_id]
for i in range(1):
    #print('Cups: {}'.format(['({})'.format(cup) if cup == current_cup else cup for cup in cups]))
    
    three_cups = [cups[(current_cup_id + i) % len(cups)] for i in range(1, 4)]
    #print('Three cups: {}'.format(three_cups))
    
    destination_cup = current_cup
    while True:
        destination_cup -= 1
        if destination_cup < MIN:
            destination_cup = MAX 
        if destination_cup not in three_cups:
            #print('Destination cup: {}'.format(destination_cup))
            for i in range(3): del cups[(cups.index(current_cup) + 1) % len(cups)]
            insert_id = cups.index(destination_cup) + 1
            break
    cups = cups[:insert_id] + three_cups + cups[insert_id:]
        
    current_cup_id = (cups.index(current_cup) + 1) % len(cups)
    current_cup = cups[current_cup_id]
        
print(time.time() - s)
