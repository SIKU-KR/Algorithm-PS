from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque([(0, 0)])
    
    while q:
        index, total = q.popleft()
        
        if index == len(numbers):
            if total == target:
                answer += 1
            continue
        
        # + 선택
        q.append((index + 1, total + numbers[index]))
        # - 선택
        q.append((index + 1, total - numbers[index]))
        
    return answer