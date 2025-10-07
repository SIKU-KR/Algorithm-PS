n, d = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]

# end가 d보다 크면 의미 없으니 제거
roads = [r for r in roads if r[1] <= d]

# 거리 dp 초기화
dp = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)  # 기본 도로 이동
    for start, end, length in roads:
        if start == i and end <= d:
            dp[end] = min(dp[end], dp[start] + length)

print(dp[d])