def solution(numbers):
    answer = []
    s = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                s.add(numbers[i] + numbers[j])
    answer = list(s)
    answer.sort()
    return answer