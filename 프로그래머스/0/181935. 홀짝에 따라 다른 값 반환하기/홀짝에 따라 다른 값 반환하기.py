def solution(n):
    if n % 2 == 1:
        answer = a(n)
    else:
        answer = b(n)
    return answer

def a(n):
    answer = 0
    while n > 0:
        if n % 2 == 1:
            answer += n
        n -= 1
    return answer

def b(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            answer += n * n
        n -= 1
    return answer
    