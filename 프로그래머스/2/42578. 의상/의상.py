def solution(clothes):
    di = {}
    for c in clothes:
        if c[1] in di:
            di[c[1]] += 1
        else:
            di[c[1]] = 1
    total = 1
    for i in list(di.values()):
        total *= (i + 1)
    return total - 1
        