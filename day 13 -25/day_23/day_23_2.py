import time

inpt = '389125467'
cups = [int(cup) for cup in inpt] + [i for i in range(10, (10 ** 6) + 1)]

MAX = max(cups)
MIN = min(cups)

# Part 1
for i in range(10):
    s = time.time()
    
    current_cup_id = 0
    #print('Cups: {}'.format(['({})'.format(cup) if cup == current_cup else cup for cup in cups]))
    
    three_cups = cups[1:4]
    #print('Three cups: {}'.format(three_cups))
    
    destination_cup = cups[0]
    while True:
        destination_cup -= 1
        if destination_cup < MIN:
            destination_cup = MAX 
        if destination_cup not in three_cups:
            #print('Destination cup: {}'.format(destination_cup)) 
            destination_cup_id = cups.index(destination_cup)
            cups = cups[4:destination_cup_id + 1] + three_cups + cups[destination_cup_id + 1:] + [cups[0]]
            break

print(time.time() - s)
