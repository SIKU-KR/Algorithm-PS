def solution(absolutes, signs):
    ans = []
    for i in range(len(absolutes)):
        s = -1
        if signs[i] == True:
            s = 1
        ans.append(absolutes[i] * s)
    return sum(ans)