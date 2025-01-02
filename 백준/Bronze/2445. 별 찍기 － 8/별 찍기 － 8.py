n = int(input())
l=[]
for i in range(n):
    str = '*'*(i+1) + ' '*(n-i-1)
    str = str + str[::-1]
    l.append(str)

for i in l:
    print(i)
for i in range(n-2, -1, -1):
    print(l[i])