import sys

input = sys.stdin.readline

n = int(input().strip())
schedule = []
for _ in range(n):
    t, p = map(int, input().strip().split())
    schedule.append((t, p))

# DP 테이블 초기화: dp[i]는 i번째 날까지 얻을 수 있는 최대 이익
dp = [0] * (n + 1)

# 각 날에 대해 DP 갱신
for i in range(n):
    t, p = schedule[i]
    # 현재 상담을 진행했을 때의 경우
    if i + t <= n:  # 상담 종료일이 기간을 초과하지 않을 때
        dp[i + t] = max(dp[i + t], dp[i] + p)
    # 현재 상담을 건너뛰었을 때의 경우
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])
