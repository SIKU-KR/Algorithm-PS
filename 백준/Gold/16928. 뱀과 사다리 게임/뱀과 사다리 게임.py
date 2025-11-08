import sys
from collections import deque

def bfs():
    deq = deque()
    deq.append([1, 0])
    visited[1] = True

    while deq:
        po, count = deq.popleft()

        if po == 100:
            print(count)
            break

        for i in range(1,7):
            newpo = po + i
            if newpo > 100:
                continue
            
            for k in range(len(s)):
                if newpo == s[k][0] and not visited[newpo]:
                    visited[newpo] = True
                    deq.append([s[k][1], count + 1])

            for j in range(len(b)):
                if newpo == b[j][0] and not visited[newpo]:
                    visited[newpo] = True
                    deq.append([b[j][1], count + 1])

            if not visited[newpo]:
                visited[newpo] = True
                deq.append([newpo, count + 1])

N, M = map(int, input().split())
visited = [False for _ in range(101)]
s = []
b = []

for i in range(N):
    s.append([int(x) for x in sys.stdin.readline().rstrip().split()])
for i in range(M):
    b.append([int(x) for x in sys.stdin.readline().rstrip().split()])

bfs()