# 순열을 만들고 (1 ~ numbers 길이) 집합으로 만듦
# 각 순열에 소수 판별 계산 적용 (2~sqrt(N)까지 나눠보기 - O(N! * SQRT N))
# 개수 반환

from itertools import permutations

def is_sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    s = set()
    for i in range(1, len(numbers) + 1):
        permutation = permutations(numbers, i)
        for p in permutation:
            tmp = int(''.join(p))
            if tmp == 0 or tmp == 1:
                continue
            if is_sosu(tmp):
                s.add(tmp)
    return len(s)