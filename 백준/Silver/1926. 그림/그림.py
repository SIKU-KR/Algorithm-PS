# boj 1926
# N = 25,000 -> O(N)

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

def bfs(i, j):
	count = 1
	queue = deque([(i, j)])
	visited[i][j] = True

	while queue:
		x, y = queue.popleft()
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x + dx, y + dy
			if 0 <= nx < n and 0 <= ny < m:
				if not visited[nx][ny] and graph[nx][ny] == 1:
					visited[nx][ny] = True
					queue.append((nx, ny))
					count += 1
	return count


cnt = 0
maxn = -1
for i in range(n):
	for j in range(m):
		if not visited[i][j] and graph[i][j] == 1:
			maxn = max(maxn, bfs(i, j))
			cnt += 1

if (cnt == 0):
	print(0)
	print(0)
else:
	print(cnt)
	print(maxn)
