def player(prev_play, opponent_history=[], PlayOrder={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    guess = 'P'

    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        PlayOrder[last_five] = PlayOrder.get(last_five, 0) + 1

        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: PlayOrder[k]
            for k in potential_plays if k in PlayOrder
        }

        if sub_order:
            guess = max(sub_order,key= sub_order.get)[-1:]

    response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return response[guess]