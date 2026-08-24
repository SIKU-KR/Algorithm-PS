from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for x in topping:
        left.add(x)
        
        right[x] -= 1
        if right[x] == 0:
            del right[x]
        if len(left) == len(right):
            answer += 1
    return answer