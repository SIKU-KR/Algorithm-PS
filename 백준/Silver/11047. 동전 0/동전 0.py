import sys

input = sys.stdin.readline

count = 0
n, k = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(n)]
coins.reverse()

for i in coins:
    if k >= i:
        count += k // i
        k = k % i

print(count)