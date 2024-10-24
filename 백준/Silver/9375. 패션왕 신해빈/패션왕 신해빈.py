t = int(input())

for i in range(t):
    n = int(input())
    dic = dict()
    for j in range(n):
        inp = input().strip().split()
        if inp[1] in dic:
            dic[inp[1]] = dic[inp[1]] + 1
        else:
            dic[inp[1]] = 1
    total = 1
    for item in dic:
        total *= dic[item] + 1
    print(total-1)
