import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

li = list(map(int, input().rstrip().split()))
start, end = 1, max(li)

while start <= end:
    mid = (start + end) // 2
    s = 0
    for i in li:
        if i >= mid:
            s += i - mid
    if s >= m:
        start = mid + 1
    else :
        end = mid - 1

print(end)
