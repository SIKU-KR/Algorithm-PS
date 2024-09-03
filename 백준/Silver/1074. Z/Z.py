# 분할 정복으로 풀기
n, r, c = map(int, input().split())

base = 0

while n > 1:
    half = 2 ** n // 2
    
    if half > r and half > c: #2사분면
        pass
    elif half > r and half <= c: #1사분면
        base += (half ** 2)
        c -= half
    elif half <= r and half > c: #3사분면
        base += (half ** 2) * 2
        r -= half
    elif half <= r and half <= c: #4사분면
        base += (half ** 2) * 3
        r -= half
        c -= half
    
    n -= 1

if r==0 and c==0:
    print(base)
elif r==0 and c==1:
    print(base+1)
elif r==1 and c==0:
    print(base+2)
elif r==1 and c==1:
    print(base+3)
else:
    print('error')