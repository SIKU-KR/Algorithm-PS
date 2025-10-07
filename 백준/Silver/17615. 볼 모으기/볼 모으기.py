n = int(input())
s = input()

def move_count(color):
    # 왼쪽으로 몰기
    left = 0
    while left < n and s[left] == color:
        left += 1
    right = n - 1
    while right >= 0 and s[right] == color:
        right -= 1
    return min(s[left:].count(color), s[:right + 1].count(color))

print(min(move_count('R'), move_count('B')))