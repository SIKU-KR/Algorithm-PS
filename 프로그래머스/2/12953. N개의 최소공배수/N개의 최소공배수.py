def solution(arr):
    a = max(arr)
    mul = 0
    while True:
        t = True
        mul += 1
        b = a * mul
        for i in arr:
            if b % i != 0:
                t = False
                break
                
        if t:
            return a * mul
                