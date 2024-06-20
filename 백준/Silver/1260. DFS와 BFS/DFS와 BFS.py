from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

# Graph base 생성
graph = []
graph.append([])
for i in range(n):
    graph.append([])

# visited 생성
visited = [False] * (n+1)

# 그래프 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 정렬
for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)