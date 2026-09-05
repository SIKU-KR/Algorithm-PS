def solution(n, lost, reserve):
    # 1. 도난당했지만 여벌이 있던 학생 제외 (순수하게 빌려야 하는 학생 / 빌려줄 수 있는 학생)
    actual_lost = sorted(list(set(lost) - set(reserve)))
    actual_reserve = sorted(list(set(reserve) - set(lost)))
    
    # 2. 앞 번호 학생부터 순차적으로 빌리기
    for r in actual_reserve:
        if r - 1 in actual_lost:
            actual_lost.remove(r - 1)
        elif r + 1 in actual_lost:
            actual_lost.remove(r + 1)
            
    # 전체 학생 수 - 끝까지 빌리지 못한 학생 수
    return n - len(actual_lost)