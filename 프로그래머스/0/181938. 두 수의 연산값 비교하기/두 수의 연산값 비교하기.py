def solution(a, b):
    ab = int(str(a) + str(b))
    twoab = 2 * a * b
    if ab >= twoab:
        return ab
    else:
        return twoab