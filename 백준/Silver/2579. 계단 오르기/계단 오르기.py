n = int(input())
li = [int(input()) for _ in range(n)]

if n == 1:
    print(li[0])
elif n == 2:
    print(li[1]+li[0])
else:
    dp = [0] * n
    dp[0] = li[0]
    dp[1] = li[1] + li[0]
    dp[2] = max(li[0]+li[2], li[1]+li[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i])
    print(dp[n-1])