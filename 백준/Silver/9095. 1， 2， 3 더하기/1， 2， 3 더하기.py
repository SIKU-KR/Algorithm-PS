t = int(input())
li = [int(input()) for _ in range(t)]
maxval = max(li)
dp = [0] * (maxval + 1)
dp[0] = 1
dp[1] = 2
if maxval > 1:
    dp[2] = 4
if maxval > 2:
    for i in range (3, maxval):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in li:
    print(dp[i-1])