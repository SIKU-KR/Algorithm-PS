def solution(n):
    if n == 2:
        return 1
    dp = [-1] * 100001
    dp[0] = 0 
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

