from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = [[-1] * m for _ in range(n)]


def bfs(i, j):
    queue = deque([(i, j)])
    answer[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and answer[nx][ny] == -1:
                answer[nx][ny] = answer[x][y] + 1
                queue.append((nx, ny))


a, b = -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer[i][j] = 0
        if graph[i][j] == 2:
            a, b = i, j

bfs(a, b)

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()
