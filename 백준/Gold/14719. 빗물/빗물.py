h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(1, w-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    if blocks[i] < left_max and blocks[i] < right_max:
        answer += min(left_max, right_max) - blocks[i]

print(answer)