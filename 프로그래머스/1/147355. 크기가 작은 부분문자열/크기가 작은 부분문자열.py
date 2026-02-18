def solution(t, p):
    answer = 0
    plen = len(p)
    pint = int(p)
    tlen = len(t)
    
    for i in range(tlen - plen + 1):
        tmp = t[i : i + plen]
        if int(tmp) <= pint:
            answer += 1
            
    return answer