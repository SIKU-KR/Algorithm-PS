def solution(land):
    dp = [land[0]]

    for i in range(1, len(land)):
        tmp = []

        for j in range(4):
            m = 0
            for k in range(4):
                if j != k:
                    m = max(m, dp[i-1][k])
            tmp.append(m + land[i][j])

        dp.append(tmp)

    return max(dp[-1])