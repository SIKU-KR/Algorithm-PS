import sys

n, m  = map(int, input().split())
a = dict()

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    a[tmp] = i+1
    a[i+1] = tmp

for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        print(a[int(tmp)])
    else:
        print(a[tmp])