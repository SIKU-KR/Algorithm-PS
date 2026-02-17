def solution(x):
    a = list(map(int, str(x)))
    d = sum(a)
    return x % d == 0