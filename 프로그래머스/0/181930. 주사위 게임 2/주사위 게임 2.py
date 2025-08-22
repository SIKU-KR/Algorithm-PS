def solution(a, b, c):
    point = validate(a, b, c)
    if point == 0:
        return a + b + c
    elif point == 1:
        return (a + b + c) * (a * a + b * b + c * c)
    else:
        return (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)

def validate(a, b, c):
    count = 0
    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1
    return count