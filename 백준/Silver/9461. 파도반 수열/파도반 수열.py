li = [1, 1, 1]
idx = 3

t = int(input())
for i in range(t):
    n = int(input()) - 1
    if idx > n:
        print(li[n])
    else:
        while idx < n + 1:
            li.append(li[idx-3] + li[idx-2])
            idx += 1
        print(li[n])