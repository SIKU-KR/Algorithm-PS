def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    while False in visited:
        answer += 1
        a = visited.index(False)
        stk = [a]
        while stk:
            t = stk.pop()
            visited[t] = True
            for i in range(len(computers[t])):
                if i == t:
                    continue
                if computers[t][i] == 1 and visited[i] == False:
                    stk.append(i)
    
    return answer