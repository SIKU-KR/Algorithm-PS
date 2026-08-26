def solution(prices):
    answer = [ -1 ] * len(prices)
    stk = [] # (값, 인덱스) 페어로 들어감
    for i in range(len(prices)):
        if stk and stk[-1][0] > prices[i]:
            std = i
            while stk and stk[-1][0] > prices[i]:
                value, index = stk.pop()
                answer[index] = std - index
        stk.append((prices[i], i))
    
    for value, index in stk:
        answer[index] = len(prices) - index - 1
    
    return answer


print(solution([4,1,4,1,4,1]))
print(solution([5,4,3,2,1]))
print(solution([1,1,1,1,1]))
print(solution([1,2,3,4,5]))