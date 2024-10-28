n, m = map(int, input().split())
li = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0

for i in li:
    tmp = tmp + i
    prefix_sum.append(tmp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])