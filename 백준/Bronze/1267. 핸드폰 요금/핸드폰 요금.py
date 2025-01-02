n = int(input())
tms = list(map(int, input().split()))

t, m = 0, 0
for i in tms:
    t += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15
if t < m:
    print('Y', t)
elif t > m:
    print('M', m)
else:
    print('Y M', t)