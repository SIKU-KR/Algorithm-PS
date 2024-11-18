from collections import deque

def bfs():
    global visited
    a = visited.index(False)
    queue = deque()
    queue.append(a)
    visited[a] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
queue = []
visited = [False] * (n+1)
visited[0] = True

while False in visited:
    count += 1
    bfs()

print(count)
