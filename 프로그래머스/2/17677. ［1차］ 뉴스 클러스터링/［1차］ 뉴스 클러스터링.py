import math
from collections import Counter

def process(s1):
    s = []
    s1 = s1.lower()
    for i in range(len(s1) - 1):
        if 'a' <= s1[i] <= 'z' and 'a' <= s1[i+1] <= 'z':
            s.append(s1[i:i+2])
    return Counter(s)

def solution(str1, str2):
    answer = 0
    s1, s2 = process(str1), process(str2)
    
    if not s1 and not s2:
        return 65536
    
    union = s1 | s2
    intersection = s1 & s2
    
    intersection_count = sum(intersection.values())
    union_count = sum(union.values())
    
    jaccard = intersection_count / union_count

    return math.trunc(jaccard * 65536)