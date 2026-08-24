def solution(s):
    answer = []
    s = s[1:-1]
    stk = []
    arr = []
    
    start = 0
    for i in range(len(s)):
        if s[i] == '{':
            start = i + 1
        elif s[i] == '}':
            tmp = s[start:i].split(',')
            tmpa = []
            for j in tmp:
                tmpa.append(int(j))
            arr.append(tmpa)
    arr.sort(key=len)
    
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
        
    return answer