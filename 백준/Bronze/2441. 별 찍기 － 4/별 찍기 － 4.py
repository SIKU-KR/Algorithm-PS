n = int(input())
cnt = 0
for i in range(n):
    str= ' '*i + '*'*(n-cnt)
    cnt += 1
    print(str)