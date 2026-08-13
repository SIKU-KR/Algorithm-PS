def solution(k, tangerine):
    d = {}
    for t in tangerine:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    
    l = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    answer = 0
    crt = 0
    for a,b in l:
        answer += 1
        crt += b
        if crt >= k:
            return answer