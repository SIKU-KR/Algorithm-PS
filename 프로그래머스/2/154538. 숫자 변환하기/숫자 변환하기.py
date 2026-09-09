def solution(x, y, n):
    dp = [ {x} ]
    if x == y:
        return 0
    idx = 1
    while True:
        tmp = set()
        for i in list(dp[idx-1]):
            a = i * 2
            b = i * 3
            c = i + n
            if a < y:
                tmp.add(a)
            if b < y:
                tmp.add(b)
            if c < y:
                tmp.add(c)
            if a == y or b == y or c == y:
                return idx      
        if len(tmp) == 0:
            return -1
        dp.append(tmp)
        idx += 1
    return -1
        