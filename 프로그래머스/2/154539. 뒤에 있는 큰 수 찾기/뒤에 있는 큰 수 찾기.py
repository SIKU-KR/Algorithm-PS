def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    
    for i in range(len(numbers)):
        n = numbers[i]
            
        while stk and numbers[stk[-1]] < n:
            answer[stk[-1]] = n
            stk.pop()
        
        stk.append(i)
        
    return answer