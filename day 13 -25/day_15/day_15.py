game = [12,20,0,6,1,17,7]

end = 30000000

game_d = {game[0]: {'last_seen': 0,
                        'index': 0}}
for i, n in enumerate(game[1:]):
    if n in game_d:
        game_d[n]['last_seen'] = game[n]['index']
        game_d[n]['index'] = i + 1
    else:
        game_d[n] = {}
        game_d[n]['last_seen'] = i + 1 
        game_d[n]['index'] = i + 1
 

current_n = game[-1]
for i in range(len(game), end):
    current_n = game_d[current_n]['index'] - game_d[current_n]['last_seen']
    if current_n in game_d:
        game_d[current_n]['last_seen'] = game_d[current_n]['index']
        game_d[current_n]['index'] = i
    else:
        game_d[current_n] = {}
        game_d[current_n]['last_seen'] = i
        game_d[current_n]['index'] = i
