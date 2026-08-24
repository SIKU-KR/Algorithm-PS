from collections import deque

def solution(priorities, location):
    answer = 0
    ansl = []
    
    p = deque(priorities)
    q = deque(list(range(0,len(priorities))))
    target = q[location]
    
    while p:
        a = max(p)
        priority, process = p.popleft(), q.popleft()
        if priority == a:
            ansl.append(process)
            continue
        p.append(priority)
        q.append(process)
        
    return ansl.index(target) + 1