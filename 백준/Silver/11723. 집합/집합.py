import sys

input = sys.stdin.readline
a = set()

n = int(input().rstrip())
for i in range(n):
    tmp = input().rstrip().split()
    s = tmp[0]
    num = int(tmp[1]) if len(tmp) > 1 else None

    if s == 'add':
        a.add(num)
    elif s == 'remove':
        a.discard(num)
    elif s == 'check':
        if num in a:
            print(1)
        else:
            print(0)
    elif s == 'toggle':
        if num in a:
            a.remove(num)
        else:
            a.add(num)
    elif s == 'all':
        a = set(range(1, 21))
    elif s == 'empty':
        a.clear()
