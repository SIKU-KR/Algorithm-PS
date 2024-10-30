# 2 * 1 -> 1개
# 2 * 2 -> 2개
# 2 * 3 -> 3개
# 2 * 4 -> 5개
# 2 * 5 -> 8개

n = int(input())
dp = [0, 1, 2]
if n >= 2:
    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-1])
print(dp[n] % 10007)