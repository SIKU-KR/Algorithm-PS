from collections import deque

def solution(maps):
    n = len(maps[0]) # 가로
    m = len(maps) # 세로
    
    dist = [[-1] * n for _ in range(m)]
    dist[0][0] = 1

    queue = deque([(0, 0)])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        crr = queue.popleft()
        x = crr[0]
        y = crr[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
                
            if maps[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append([nx, ny])
    
    return dist[m-1][n-1]