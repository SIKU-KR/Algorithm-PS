n = int(input())
l = []
cnt = n-1
for i in range(n):
    str= ' '*cnt + '*'*(n-cnt) + '*'*i
    cnt -= 1
    l.append(str)
for i in range(len(l)-1, -1, -1):
    print(l[i])