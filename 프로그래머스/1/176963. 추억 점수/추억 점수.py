def solution(name, yearning, photo):
    answer = []
    yd = {}
    for i in range(len(name)):
        yd[name[i]] = yearning[i]
    for p in photo:
        temp = 0
        for f in p:
            if f not in yd:
                continue
            temp += yd[f]
        answer.append(temp)
    
    return answer