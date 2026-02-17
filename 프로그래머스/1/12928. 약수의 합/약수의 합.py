import math

def solution(n):
    if n == 0: return 0
    divisors = set()
    
    # 1부터 root n까지만 확인하면 모든 약수를 찾을 수 있습니다.
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)  # set이라서 중복은 자동으로 제거됩니다.
            
    return sum(divisors)