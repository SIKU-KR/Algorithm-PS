import sys

input = sys.stdin.readline

n = int(input().rstrip())
li = list(map(int, input().rstrip().split()))

li.sort()
dp = [li[0], ]

for i in range(1, n):
    dp.append(dp[i-1] + li[i])

sum = 0
for i in dp:
    sum += i
print(sum)