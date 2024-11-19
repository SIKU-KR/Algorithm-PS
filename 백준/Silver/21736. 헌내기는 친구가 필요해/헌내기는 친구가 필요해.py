from collections import deque

def bfs():
    count = 0
    visited = [[False] * m for _ in range(n)]
    que = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'I':
                x, y = j, i
                break

    que.append((x, y))
    visited[y][x] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and not visited[new_y][new_x] and graph[new_y][new_x] != 'X':
                visited[new_y][new_x] = True
                if graph[new_y][new_x] == 'P':
                    count += 1
                que.append((new_x, new_y))
    
    return count

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])
    string = input()
    for c in string:
        graph[i].append(c)

ans = bfs()
if ans == 0:
    print('TT')
else:
    print(ans)
