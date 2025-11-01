from bisect import bisect_left
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

names = []
powers = []

for i in range(n):
    name, power = input().split()
    power = int(power)
    if not powers or power != powers[-1]:
        names.append(name)
        powers.append(power)

for i in range(m):
    s = int(input().rstrip())
    idx = bisect_left(powers, s)
    print(names[idx])
        
        