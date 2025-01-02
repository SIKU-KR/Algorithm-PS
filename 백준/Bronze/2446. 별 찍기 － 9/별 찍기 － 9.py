n = int(input())
l = []

# 상단 부분
for i in range(n):
    stars = '*' * (2 * (n - i) - 1)
    line = ' ' * i + stars
    l.append(line)

# 출력
for i in l:
    print(i)

# 하단 부분
for i in range(n - 2, -1, -1):
    print(l[i])
