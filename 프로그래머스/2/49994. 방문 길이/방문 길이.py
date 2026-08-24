def solution(dirs):
    answer = 0
    x, y = 0, 0
    visited = set()
    
    for ch in dirs:
        nx, ny = x, y
        if ch == 'U' and ny <= 4:
            ny += 1
        elif ch == 'D' and ny >= -4:
            ny -= 1
        elif ch == 'R' and nx <= 4:
            nx += 1
        elif ch == 'L' and nx >= -4:
            nx -= 1
            
        if (nx, ny) == (x, y):
            continue
            
        path1 = (x, y, nx, ny)
        path2 = (nx, ny, x, y)

        if path1 not in visited:
            answer += 1
            visited.add(path1)
            visited.add(path2)
        
        x, y = nx, ny

    return answer