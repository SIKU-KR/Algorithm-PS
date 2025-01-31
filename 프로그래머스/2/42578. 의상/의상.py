from itertools import combinations

def solution(clothes):
    clcnt = {}
    for i, j in clothes:
        if j in clcnt.keys():
            clcnt[j] += 1
        else:
            clcnt[j] = 2
    ans = 1
    for k in clcnt.keys():
        ans *= clcnt[k]
    answer = ans - 1
    return answer