import math

n, k = map(int, input().split())
p = {}

for _ in range(n):
    str = input()
    if str in p:
        p[str] += 1
    else:
        p[str] = 1

cnt = 0
for v in p.values():
    cnt += math.ceil(v/k)
print(cnt)