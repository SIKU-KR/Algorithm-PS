import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
data = dict()
for i in range(n):
    inp = input().rstrip().split()
    data[inp[0]] = inp[1]

for i in range(m):
    inp = input().rstrip()
    print(data[inp])
