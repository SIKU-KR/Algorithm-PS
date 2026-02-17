import math

def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        if math.sqrt(i).is_integer():
            sum -= i
        else:
            sum += i
    return sum