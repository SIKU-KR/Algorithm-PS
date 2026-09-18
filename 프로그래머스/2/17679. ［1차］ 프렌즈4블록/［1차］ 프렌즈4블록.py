def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        li = []
        for i in range(m-1):
            for j in range(n-1):
                a = board[i][j]
                if a == '0':
                    continue
                if board[i+1][j] == a and board[i][j+1] == a and board[i+1][j+1] == a:
                    li.append((i, j))
                    li.append((i+1, j))
                    li.append((i, j+1))
                    li.append((i+1, j+1))
        if len(li) == 0:
            return answer
        while li:
            x, y = li.pop()
            if board[x][y] == '0':
                continue
            board[x][y] = '0'
            answer += 1
        for i in range(n):
            a = []
            for j in range(m):
                if board[j][i] != '0':
                    a.append(board[j][i])
            cnt = m - len(a)
            a = (['0'] * cnt) + a
            for j in range(m):
                board[j][i] = a[j]
    print(board)
    return answer