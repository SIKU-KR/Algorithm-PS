def solution(number):
    answer = 0
    
    for i in range(len(number)):
        for j in range(i, len(number)):
            for k in range(j, len(number)):
                if not (i == j or j == k or k == i):
                    if number[i] + number[j] + number[k] == 0:
                        answer += 1
    
    return answer