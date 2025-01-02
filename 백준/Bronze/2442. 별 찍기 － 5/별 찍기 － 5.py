n = int(input())
cnt = n-1
for i in range(n):
    str= ' '*cnt + '*'*(n-cnt) + '*'*i
    cnt -= 1
    print(str)