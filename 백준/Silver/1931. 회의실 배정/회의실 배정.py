import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = [[0]*2 for _ in range(n)]

for i in range(n):
    x, y = map(int, input().rstrip().split())
    a[i][0] = x
    a[i][1] = y

a.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = a[0][1]
for i in range(1, n):
    if a[i][0] >= end_time:
        cnt += 1
        end_time = a[i][1]

print(cnt)