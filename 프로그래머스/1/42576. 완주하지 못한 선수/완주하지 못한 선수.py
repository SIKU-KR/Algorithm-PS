from collections import Counter

def solution(participant, completion):
    s = Counter(participant)
    for c in completion:
        s[c] -= 1
        
    return s.most_common(1)[0][0]