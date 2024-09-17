from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    visited = [False] * (cn+1)
    visited[1] = True
    count = 0
    while queue:
        a = queue.popleft()
        count += 1
        for i in graph[a]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return count - 1
    

cn = int(input())
pn = int(input())

graph = [[] for _ in range(cn+1)]
for i in range(pn):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())
