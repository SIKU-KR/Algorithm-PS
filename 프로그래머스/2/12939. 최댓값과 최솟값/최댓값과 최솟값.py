def solution(s):
    ar = list(map(int, s.split()))
    return str(min(ar)) + ' ' + str(max(ar))