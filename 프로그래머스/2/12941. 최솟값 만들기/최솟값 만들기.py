def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i in range(0, len(A)):
        sum += A[i] * B[i]
    return sum