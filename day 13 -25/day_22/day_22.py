from copy import deepcopy

with open("day_22.txt") as f:
    game = f.read().splitlines()

deck_1 = list()
for i in range(1, len(game)):
    if game[i].isdigit():
        deck_1.append(int(game[i]))
    else:
        break

deck_2 = list()
for j in range(i + 2, len(game)):
    if game[j].isdigit():
        deck_2.append(int(game[j]))
    else:
        break

deck_1 = deck_1[::-1]
deck_2 = deck_2[::-1]

'''
## Part 1
while deck_1 and deck_2:
    draw_card_1 = deck_1.pop()
    draw_card_2 = deck_2.pop()

    if max(draw_card_1, draw_card_2) == draw_card_1:
        deck_1.insert(0, draw_card_1)
        deck_1.insert(0, draw_card_2)
    else:
        deck_2.insert(0, draw_card_2)
        deck_2.insert(0, draw_card_1)

if deck_1: winner_deck = deck_1
else: winner_deck = deck_2

score = sum([(i + 1) * winner_deck[i] for i in range(len(winner_deck))])
'''

## Part 2
def recursive_combat(deck_1, deck_2,
                     original_deck_1 = None, original_deck_2 = None,
                     suspended_card_1=None, suspended_card_2 = None,
                     game=1):
    #print(' -- Starting game {} --'.format(game))
    previous_decks = set()
    winner = None
    
    while True:
        compact_decks = ''.join([str(card) for card in deck_1 + deck_2])

        #print('Player 1: {} \nPlayer 2: {}'.format(deck_1, deck_2))
        
        if not deck_1:
            winner = 2
            break
        elif not deck_2:
            winner= 1
            break
        elif compact_decks in previous_decks:
            #print('Game: {} - Avoiding loop, player 1 wins'.format(game))
            winner = 1
            break

        previous_decks.add(compact_decks)

        draw_card_1 = deck_1.pop()
        draw_card_2 = deck_2.pop()

        #print('Player 1: card: {} \nPlayer 2: card: {}'.format(draw_card_1, draw_card_2))
        
        if draw_card_1 < len(deck_1) + 1 and draw_card_2 < len(deck_2) + 1:
            #print('Entering subgame \n--------------')
            _, deck_1, deck_2 = recursive_combat(deck_1, deck_2,
                                                 deepcopy(deck_1), deepcopy(deck_2),
                                                 draw_card_1, draw_card_2,
                                                 game + 1)
        elif max(draw_card_1, draw_card_2) == draw_card_1:
            deck_1.insert(0, draw_card_1)
            deck_1.insert(0, draw_card_2)
            #print('Player 1 wins \n')
        elif max(draw_card_1, draw_card_2) == draw_card_2:
            deck_2.insert(0, draw_card_2)
            deck_2.insert(0, draw_card_1)
            #print('Player 2 wins \n')

    if suspended_card_1 and suspended_card_2:
        if winner == 1:
            original_deck_1.insert(0, suspended_card_1)
            original_deck_1.insert(0, suspended_card_2)
            #if game > 1: print('Going back to previous game...')
            return winner, original_deck_1, original_deck_2
        elif winner == 2:
            original_deck_2.insert(0, suspended_card_2)
            original_deck_2.insert(0, suspended_card_1)
            #if game > 1: print('Going back to previous game...')
            return winner, original_deck_1, original_deck_2

    return winner, deck_1, deck_2

winner, final_1, final_2 = recursive_combat(deck_1, deck_2)
if winner == 1: score = sum([(i + 1) * final_1[i] for i in range(len(final_1))])
else: score = sum([(i + 1) * final_2[i] for i in range(len(final_2))])
print(score)
    
        

