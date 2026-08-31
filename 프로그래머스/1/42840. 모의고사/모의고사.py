def player1(length):
    a = []
    while len(a) < length:
        a += [1,2,3,4,5]
    return a[:length]

def player2(length):
    a = []
    while len(a) < length:
        a += [2,1,2,3,2,4,2,5]
    return a[:length]

def player3(length):
    a = []
    while len(a) < length:
        a += [3,3,1,1,2,2,4,4,5,5]
    return a[:length]

def solution(answers):
    p1 = player1(len(answers))
    p2 = player2(len(answers))
    p3 = player3(len(answers))
    scores = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]
        if p1[i] == answer:
            scores[0] += 1
        if p2[i] == answer:
            scores[1] += 1
        if p3[i] == answer:
            scores[2] += 1
    
    answer = []
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer