n = int(input())
li = list(map(int, input().split()))

li.sort()

left = 0
right = n - 1

result = [li[left], li[right]]
while left < right:
    sum = li[left] + li[right]
    if abs(sum) < abs(result[0] + result[1]):
        result = [li[left], li[right]]
    if sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])