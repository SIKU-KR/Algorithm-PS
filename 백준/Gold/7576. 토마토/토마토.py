# boj 7576
# N <= 1,000,000 , O(N) 

from collections import deque

m, n = map(int, input().split())
graph = []
total_unripe = 0
ones_loc = deque([])
visited = [[False] * m for _ in range(n)]

# O(N)
for i in range(n):
	a = list(map(int, input().split()))
	
	for j in range(m):
		if a[j] == 1:
			ones_loc.append((i, j))
		elif a[j] == 0:
			total_unripe += 1

	graph.append(a)

if total_unripe == 0:
	print(0)
	exit(0)

days = -1

def bfs(i, j):
	global total_unripe

	visited[i][j] = True
	for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		nx, ny = i + dx, j + dy
		if 0 <= nx < n and 0 <= ny < m:
			if visited[nx][ny] == False and graph[nx][ny] == 0:
				visited[nx][ny] = True
				graph[nx][ny] = 1
				ones_loc.append((nx, ny))
				total_unripe -= 1

while True:
	days += 1
	cnt = len(ones_loc)
	for i in range(cnt):
		c, d = ones_loc.popleft()
		bfs(c, d)
	if not ones_loc:
		break


if total_unripe == 0:
    print(days)
else:
    print(-1)
