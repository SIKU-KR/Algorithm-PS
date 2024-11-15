import sys
import heapq

input = sys.stdin.readline

que = []
heap = []

n = int(input().rstrip())
for i in range(n):
    x = int(input().rstrip())
    que.append(x)

while len(que) != 0:
    a = que.pop(0)
    if a == 0:
        if(len(heap) == 0):
            print(0)
        else:
            print((heapq.heappop(heap) * -1))
    else:
        heapq.heappush(heap, (a * -1))