import sys
input = sys.stdin.readline

n = int(input())
bldg = []
for i in range(n):
    bldg.append(int(input()))

cnt = 0
stack = []
for i in bldg:
    while stack and stack[-1] <= i:
        stack.pop()
    cnt += len(stack)
    stack.append(i)

print(cnt)