def solution(board, h, w):
    n = len(board)
    answer = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(0, 4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh >= 0 and nh < n and nw >= 0 and nw < n:
            if board[h][w] == board[nh][nw]:
                answer += 1
    return answer