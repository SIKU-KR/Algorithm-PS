def one_count(a):
    return bin(a).count('1')

def solution(n):
    q = one_count(n)
    while True:
        n += 1
        if one_count(n) == q:
            return n
        