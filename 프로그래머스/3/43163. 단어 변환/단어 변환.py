from collections import Counter
from collections import deque

def diff(str1, str2):
    a = Counter(str1)
    b = Counter(str2)
    c = a - b
    return sum(c.values())

def solution(begin, target, words):
    words = [ begin ] + words
    start = 0
    q = deque( [(start, 0)] )
    visited = [False] * len(words)
    while q:
        index, count = q.popleft()
        visited[index] = True
        for i in range(len(words)):
            if words[index] == words[i]:
                continue
            if diff(words[index], words[i]) == 1 and not visited[i]:
                q.append((i, count + 1))
                if words[i] == target:
                    return count + 1
    return 0
