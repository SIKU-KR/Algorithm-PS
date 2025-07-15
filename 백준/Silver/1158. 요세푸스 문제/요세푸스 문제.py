# boj 1158
# N = 5000, O(N^2)

n, k = map(int, input().split())

arr = list(range(1, n + 1))
ans = []
idx = 0

while arr:
	idx = (idx + k - 1) % len(arr)
	ans.append(arr.pop(idx))

print("<" + ", ".join(map(str, ans)) + ">")
