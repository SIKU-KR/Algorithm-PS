def solution(n, m):
    i = min(n, m)
    while i > 0:
        if n % i == 0 and m % i == 0:
            break
        i -= 1
    
    j = max(n, m)
    while True:
        if j % n == 0 and j % m == 0:
            break
        j += 1
    return [ i, j ]