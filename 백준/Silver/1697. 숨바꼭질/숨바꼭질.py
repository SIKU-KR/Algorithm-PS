from collections import deque

def bfs(a):
    queue = deque()
    queue.append(n)
    a[n] = 0
    while queue:
        v = queue.popleft()
        if v == k:
            return a[v]            
        for i in (v+1, v-1, v*2):
            if 0 <= i <= 100000 and a[i] == 0:
                a[i] = a[v] + 1
                queue.append(i)

n, k = map(int, input().split())
a = [0] * 100001
print(bfs(a))