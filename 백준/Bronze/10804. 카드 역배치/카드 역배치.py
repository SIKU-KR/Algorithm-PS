a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(10):
    n, m = map(int, input().split())
    a = a[:n] + a[n:m+1][::-1] + a[m+1:]
for i in range(1, len(a)):
    print(a[i], end=' ')