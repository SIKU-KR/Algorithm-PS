def solution(triangle):
    dp = [ triangle[0] ]
    
    for i in range(1, len(triangle)):    
        tmp = []
        for j in range(i+1):
            val = 0
            if j == 0:
                val = triangle[i][j] + dp[i-1][j]
            elif j >= 1 and j < i:
                val = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            else:
                val = triangle[i][j] + dp[i-1][j-1]
            tmp.append(val)
        dp.append(tmp)
    return max(dp[-1])