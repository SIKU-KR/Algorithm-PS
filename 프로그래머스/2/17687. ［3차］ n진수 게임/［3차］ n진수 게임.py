def change(num, n):
    string = "0123456789ABCDEF"
    result = ""
    while num > 0:
        result = string[num % n] + result
        num //= n
    return result

def solution(n, t, m, p):
    answer = ""
    original = "0"
    i, current = 1, 0
    p -= 1
    
    while len(answer) < t:
        if current == len(original):
            original += change(i, n)
            i += 1
        if current % m == p:
            answer += original[current]
            # print(current,original, answer)
        current += 1
    
    return answer