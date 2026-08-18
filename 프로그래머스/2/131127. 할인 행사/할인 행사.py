from collections import Counter

def solution(want, number, discount):
    answer = 0
    d = {}
    
    for i in range(0, len(want)):
        d[want[i]] = number[i]
    for i in range(0, len(discount) - 9):
        target = discount[i:i+10]
        cnt = Counter(target)
        if d == cnt:
            answer += 1
    
    return answer