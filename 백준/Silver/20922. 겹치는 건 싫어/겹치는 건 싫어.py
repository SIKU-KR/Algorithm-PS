import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

from collections import defaultdict
cnt = defaultdict(int)

l = 0
best = 0
for r in range(n):
    cnt[a[r]] += 1
    # 제약 위반이면 왼쪽을 줄여서 해소
    while cnt[a[r]] > k:
        cnt[a[l]] -= 1
        l += 1
    # 여기서 [l..r]는 각 값이 k번 이하
    best = max(best, r - l + 1)

print(best)