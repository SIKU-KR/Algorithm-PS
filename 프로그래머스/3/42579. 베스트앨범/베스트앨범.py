def solution(genres, plays):
    total = {}
    pandn = {}
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]
        if genres[i] in pandn:
            pandn[genres[i]].append((plays[i], i))
        else:
            pandn[genres[i]] = []
            pandn[genres[i]].append((plays[i], i))
    for key in pandn.keys():
        pandn[key].sort(key=lambda x: (-x[0], x[1]))
    keys = sorted(total, key=total.get, reverse=True)
    answer = []
    for key in keys:
        target = pandn[key]
        answer.append(target[0][1])
        if len(target) > 1:
            answer.append(target[1][1])
    return answer