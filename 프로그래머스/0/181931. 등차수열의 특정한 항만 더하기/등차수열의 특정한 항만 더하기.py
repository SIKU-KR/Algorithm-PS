def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += getNumber(a, d, i)
    return answer

def getNumber(a, d, idx):
    return a + d * idx