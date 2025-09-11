def solution(players, callings):
    d = {}
    for i in range(len(players)):
        d[players[i]] = i
    for i in callings:
        a = d[i]
        b_name = players[a-1]
        b = d[b_name]
        players[a], players[a-1] = players[a-1], players[a]
        d[i], d[b_name] = d[b_name], d[i]        
    return players