n, m = map(int, input().split())
a = set()
b = set()

for i in range(n):
    a.add(input())
for i in range(m):
    b.add(input())

c = a & b
li = list(c)
li = sorted(li)
print(len(li))
for i in li:
    print(i)