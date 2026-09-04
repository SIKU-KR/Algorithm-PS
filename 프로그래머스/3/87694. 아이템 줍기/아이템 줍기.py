from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[-1] * 105 for _ in range(105)]
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if i == x1 or i == x2 or j == y1 or j == y2:
                    if grid[j][i] != -2:
                        grid[j][i] = 0
                else:
                    grid[j][i] = -2
    cX, cY, iX, iY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    d = [ (1,0), (-1,0), (0,1), (0,-1)]
    
    q = deque()
    q.append((cX, cY))
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            x1, y1 = x + dx, y + dy 
            if x1 == cX and y1 == cY:
                continue
            if grid[y1][x1] == 0:
                grid[y1][x1] = grid[y][x] + 1
                q.append((x1, y1))
                if x1 == iX and y1 == iY:
                    return grid[y1][x1] // 2
            
            