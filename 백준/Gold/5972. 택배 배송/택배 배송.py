import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


distance = [float('inf')] * (n + 1)
distance[1] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, j in graph[now]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(1)
print(distance[n])