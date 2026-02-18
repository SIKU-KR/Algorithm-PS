def solution(d, budget):
    t = 0
    answer = 0
    d.sort()
    for i in d:
        if t + i <= budget:
            answer += 1
            t += i
    return answer