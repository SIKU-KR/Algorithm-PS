import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input().rstrip())
for i in range(n):
    tmp = int(input().rstrip())
    if tmp == 0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, tmp)

