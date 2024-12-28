# https://www.acmicpc.net/problem/2578

import sys

bingo = [[False for _ in range(5)] for _ in range(5)]
data = {}

def isBingo():
    global bingo
    bingo_count = 0

    # 가로 빙고 확인
    for row in bingo:
        if all(row):  # 한 줄이 모두 True
            bingo_count += 1

    # 세로 빙고 확인
    for col in range(5):
        if all(bingo[row][col] for row in range(5)):
            bingo_count += 1

    # 대각선 빙고 확인 (왼쪽 위에서 오른쪽 아래)
    if all(bingo[i][i] for i in range(5)):
        bingo_count += 1

    # 대각선 빙고 확인 (오른쪽 위에서 왼쪽 아래)
    if all(bingo[i][4 - i] for i in range(5)):
        bingo_count += 1

    # 빙고가 3개 이상이면 True 반환
    return bingo_count >= 3

# 입력 처리
for row in range(5):
    line = input().split()
    for col, num in enumerate(line):
        data[int(num)] = (row, col)

count = 0
for _ in range(5):
    line = input().split()
    for num in line:
        count += 1
        if int(num) in data:
            row, col = data[int(num)]
            bingo[row][col] = True
            if isBingo():
                print(count)
                sys.exit()
