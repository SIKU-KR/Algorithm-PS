n = []
for i in range(9):
    a = int(input())
    n.append(a)

def find():
    global n
    total = sum(n)
    for i in n:
        for j in n:
            if i == j:
                continue
            if total - i - j == 100:
                n.remove(i)
                n.remove(j)
                return

find()
n.sort()
for i in n:
    print(i)
